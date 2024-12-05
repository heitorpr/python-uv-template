from sqlmodel import Field, SQLModel


class MissionBase(SQLModel):
    name: str
    description: str


class Mission(MissionBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
