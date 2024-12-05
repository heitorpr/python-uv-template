from app.domain.models.hero import HeroBase
from app.domain.models.mission import MissionBase
from app.domain.models.team import TeamBase


class HeroPublic(HeroBase):
    team: TeamBase | None = None


class TeamPublic(TeamBase):
    heroes: list[HeroBase] | None = None


class MissionPublic(MissionBase):
    heroes: list[HeroPublic] = []
