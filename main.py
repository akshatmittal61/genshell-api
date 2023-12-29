from typing import Union
from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/api/v1/generate-command")
def generate_command(body = Body(...)):
    try:
        # get prompt from body
        prompt = jsonable_encoder(body)
        # generate command
        return {"command": "echo " + prompt["prompt"]}
    except Exception as e:
        return {"error": str(e)}
    