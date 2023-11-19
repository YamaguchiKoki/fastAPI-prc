from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    title: str
    published: Union[str, None] = None
    body: str

app = FastAPI()

@app.post("/items")
async def create_item(request: Item):
    result = {'data': f"Item is created as {request.body}"}
    return result
    