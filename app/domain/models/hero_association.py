from sqlmodel import Field, Relationship, SQLModel


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=255, index=True)
    heroes: list["Hero"] = Relationship(back_populates="team")


class HeroMissionLink(SQLModel, table=True):
    hero_id: int | None = Field(default=None, foreign_key="hero.id", primary_key=True)
    mission_id: int | None = Field(default=None, foreign_key="mission.id", primary_key=True)


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=255, index=True)
    secret_name: str = Field(unique=True, max_length=255)
    age: int | None = None
    team_id: int | None = Field(default=None, foreign_key="team.id")
    team: Team | None = Relationship(back_populates="heroes")
    missions: list["Mission"] = Relationship(back_populates="heroes", link_model=HeroMissionLink)


class Mission(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str = Field(max_length=255)
    heroes: list[Hero] = Relationship(back_populates="missions", link_model=HeroMissionLink)
