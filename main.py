from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    