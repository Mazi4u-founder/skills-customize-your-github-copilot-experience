from typing import Dict, Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float = 0.0


store: Dict[int, Item] = {}
next_id = 1


@app.post("/items", response_model=Item)
def create_item(item: Item):
    global next_id
    item.id = next_id
    store[next_id] = item
    next_id += 1
    return item


@app.get("/items", response_model=List[Item])
def list_items():
    return list(store.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = store.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    stored = store.get(item_id)
    if not stored:
        raise HTTPException(status_code=404, detail="Item not found")
    item.id = item_id
    store[item_id] = item
    return item


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in store:
        del store[item_id]
        return {"ok": True}
    raise HTTPException(status_code=404, detail="Item not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
