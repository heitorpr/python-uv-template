from src.domain.models.hero import HeroBase
from src.domain.models.mission import MissionBase
from src.domain.models.team import TeamBase


class HeroPublic(HeroBase):
    team: TeamBase | None = None


class TeamPublic(TeamBase):
    heroes: list[HeroBase] | None = None


class MissionPublic(MissionBase):
    heroes: list[HeroBase] = []
