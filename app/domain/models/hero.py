from sqlmodel import Field, SQLModel


class HeroBase(SQLModel):
    name: str
    secret_name: str
    age: int | None = None


class HeroCreate(HeroBase):
    team_id: int | None = Field(default=None)
