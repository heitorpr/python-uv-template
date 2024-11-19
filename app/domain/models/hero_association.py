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


class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    team_id: int | None = Field(default=None, foreign_key="team.id")
    team: Team | None = Relationship(back_populates="heroes")
