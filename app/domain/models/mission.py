from sqlmodel import SQLModel


class MissionBase(SQLModel):
    name: str
    description: str
