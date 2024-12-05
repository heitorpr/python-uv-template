from sqlmodel import Field, SQLModel


class TeamBase(SQLModel):
    name: str = Field(index=True)
    headquarters: str
