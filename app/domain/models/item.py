from app.domain.models import SQLModel


class Item(SQLModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
