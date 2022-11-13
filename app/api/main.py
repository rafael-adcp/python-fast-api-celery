from typing import Union

from fastapi import FastAPI

from app.workers.tasks import add, hello

app = FastAPI()

@app.get("/")
def read_root():
    print('deveria colocar na fila')
    print(add)
    add.delay(5,7)
    return {"Hello": "World"}

@app.get("/test")
def read_root():
    print('deveria colocar na fila')
    hello.delay()
    return {"/test funcionou"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
