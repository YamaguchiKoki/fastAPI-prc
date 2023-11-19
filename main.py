from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_name}")
async def index(item_name: int):
    return {"item_name" : item_name}