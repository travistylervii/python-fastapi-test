from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ytid/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):

    #processes youtube transcript from id
   
    #return transcript string

    #testing

    speak = "I have nothing to say"


    if item_id < 10:
        speak = "Item is less than 10"
    if item_id >= 10 and item_id < 20:
        speak = "Item is between 10 and 20"
    if item_id >= 20:
        speak = "item is 20 or over"

    return {"item_id": item_id, "output": speak}