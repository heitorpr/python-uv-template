from sqlmodel import Field, SQLModel

from app.domain.models.team import TeamCreate


class HeroBase(SQLModel):
    name: str = Field(title="Hero name", description="Hero real name")
    secret_name: str = Field(title="Hero secret name", description="Hero secret name")
    age: int | None = Field(default=None, title="Hero age", description="Hero age")


class Hero(HeroBase, table=True):
    id: int = Field(primary_key=True)
    team_id: int | None = Field(default=None, foreign_key="team.id")


class HeroMissionLink(SQLModel, table=True):
    hero_id: int = Field(
        title="Hero id",
        description="Hero identification",
        primary_key=True,
        foreign_key="hero.id",
    )
    mission_id: int = Field(
        title="Mission id",
        description="Mission identification",
        primary_key=True,
        foreign_key="mission.id",
    )


class HeroCreate(HeroBase):
    team_id: int | None = Field(
        default=None, title="Team ID", description="The ID of the team the hero is in"
    )
    team: TeamCreate | None = Field(
        default=None,
        title="Team",
        description="The team the hero is in, it will be created together",
    )


class HeroUpdate(HeroBase):
    team_id: int | None = Field(
        default=None, title="Team ID", description="The ID of the team the hero is in"
    )
