from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root() -> dict:
    return hello_world()


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None) -> dict:
    return {"item_id": item_id, "q": q}


def hello_world() -> dict:
    return {"Hello": "World"}
