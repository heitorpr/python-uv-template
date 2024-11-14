from sqlmodel import Field, Relationship, SQLModel

from app.domain.models.user import User

from .item import Item


# Broken
class Order(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    user: User = Relationship(cascade_delete=True, link_model=User)
    items: list[Item] = Relationship(link_model=Item)
