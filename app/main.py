from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from app.domain.models import Item

app = FastAPI(default_response_class=ORJSONResponse)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.get(
    "/items",
    summary="Read items",
    description=(
        "Read items with all the information, including their name, description, price and tax."
    ),
    tags=["items"],
    response_model=list[Item],
    status_code=200,
)
async def read_items():
    item1 = Item(name="Foo", price=50)
    item2 = Item(name="Bar", price=75, tax=5)

    return [item1, item2]
