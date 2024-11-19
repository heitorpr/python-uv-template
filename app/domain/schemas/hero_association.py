from app.domain.models.hero_association import HeroBase, Mission, MissionBase, Team


class HeroSchema(HeroBase):
    id: int | None = None
    team: Team | None = None
    missions: list[Mission]


class MissionSchema(MissionBase):
    heroes: list[HeroBase]
