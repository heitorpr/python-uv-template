from sqlmodel import Field, SQLModel


class MissionBase(SQLModel):
    name: str
    description: str


class Mission(MissionBase, table=True):
    id: int = Field(primary_key=True)


class MissionCreate(MissionBase):
    pass
