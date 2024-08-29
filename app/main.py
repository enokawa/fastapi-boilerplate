from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root() -> Dict:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None) -> Dict:
    return {"item_id": item_id, "q": q}
