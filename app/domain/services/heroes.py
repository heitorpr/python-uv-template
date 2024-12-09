from app.api.v1.schemas import HeroPublic
from app.domain.models import Hero, Team
from app.domain.models.hero import HeroCreate, HeroUpdate
from app.domain.repositories import HeroesRepository, TeamsRepository


class HeroesService:
    def __init__(self, hero_repository: HeroesRepository, team_repository: TeamsRepository):
        self.hero_repository = hero_repository
        self.team_repository = team_repository

    async def _parse_to_public(self, hero: Hero, team: Team | None = None) -> HeroPublic:
        if hero.team_id and not team:
            team = await self.team_repository.get(hero.team_id)

        return HeroPublic(**{**hero.model_dump(), "team": team.model_dump() if team else None})

    async def create(self, hero_create: HeroCreate) -> HeroPublic:
        if hero_create.team_id and hero_create.team:
            raise ValueError("You can't pass both team_id and team")

        if hero_create.team:
            team = await self.team_repository.create(hero_create.team)
            hero_create.team_id = team.id

        hero = await self.hero_repository.create(hero_create)
        return await self._parse_to_public(hero)

    async def create_list(self, hero_create_list: list[HeroCreate]) -> list[HeroPublic]:
        # Remove duplicates teams by creating a map using the team name as key
        teams_map = {item.team.name: item.team for item in hero_create_list if item.team}

        created_teams = await self.team_repository.create_list(list(teams_map.values()))

        # Create a map to easily access the team by name
        teams_created_map = {team.name: team for team in created_teams}

        for hero_create in hero_create_list:
            if hero_create.team:
                hero_create.team_id = teams_created_map[hero_create.team.name].id

        heroes = await self.hero_repository.create_list(hero_create_list)

        """
        To respond with the team data, we need to create a map using the team_id as key,
        this avoids hitting db again to get the team
        """
        teams_id_map = {team.id: team for team in created_teams}

        return [
            await self._parse_to_public(hero, teams_id_map[hero.team_id] if hero.team_id else None)
            for hero in heroes
        ]

    async def get(self, hero_id: int) -> HeroPublic:
        hero = await self.hero_repository.get(hero_id)
        return await self._parse_to_public(hero)

    async def update(self, hero_id: int, hero_data: HeroUpdate) -> HeroPublic:
        hero = await self.hero_repository.update(hero_id, hero_data)
        return await self._parse_to_public(hero)

    async def delete(self, hero_id: int) -> HeroPublic:
        hero = await self.hero_repository.delete(hero_id)
        return await self._parse_to_public(hero)

    async def assign_team(self, hero_id: int, team_id: int) -> HeroPublic:
        hero = await self.hero_repository.get(hero_id)
        team = await self.team_repository.get(team_id)

        hero.team_id = team.id
        await self.hero_repository.update(hero_id, HeroUpdate(**hero.model_dump()))
        return await self._parse_to_public(hero)
