from sqlmodel import Field, SQLModel


class TeamBase(SQLModel):
    name: str = Field(title="Team name", description="Team name", index=True, unique=True)
    headquarters: str = Field(title="Team headquarters", description="Team headquarters")


class Team(TeamBase, table=True):
    id: int = Field(title="Team id", description="Team identification", primary_key=True)


class TeamCreate(TeamBase):
    pass


class TeamUpdate(TeamBase):
    pass
