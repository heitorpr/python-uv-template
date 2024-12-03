from sqlmodel import Field, Relationship, SQLModel


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str
    heroes: list["Hero"] = Relationship(back_populates="team")


class HeroBase(SQLModel):
    name: str
    secret_name: str
    age: int | None = None


class HeroCreate(HeroBase):
    pass


class HeroMissionLink(SQLModel, table=True):
    hero_id: int = Field(default=None, primary_key=True, foreign_key="hero.id")
    mission_id: int = Field(default=None, primary_key=True, foreign_key="mission.id")


class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    team_id: int | None = Field(default=None, foreign_key="team.id")
    team: Team | None = Relationship(back_populates="heroes")
    missions: list["Mission"] = Relationship(back_populates="heroes", link_model=HeroMissionLink)


class MissionBase(SQLModel):
    name: str
    description: str


class Mission(MissionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    heroes: list[Hero] = Relationship(back_populates="missions", link_model=HeroMissionLink)
