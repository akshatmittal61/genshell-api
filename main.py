from fastapi import FastAPI, Request, Response, Body, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from utils import HTTP

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
def generate_command(request: Request, response: Response, body = Body(...)):
    http = HTTP(response)
    try:
        # get prompt from body
        req_body = jsonable_encoder(body)
        prompt = req_body.get("prompt", None)
        os = req_body.get("os", "linux")
        if not prompt:
            return http.response(status.HTTP_400_BAD_REQUEST, "Prompt is required")
        if os not in ["windows", "linux", "mac"]:
            return http.response(status.HTTP_400_BAD_REQUEST, "Please select a valid operating system")
        if prompt == "moron":
            return http.response(status.HTTP_406_NOT_ACCEPTABLE, "denied processing offensive words")
        # generate command
        return http.response(status.HTTP_200_OK, "echo " + prompt)
    except Exception as e:
        return http.response(status.HTTP_500_INTERNAL_SERVER_ERROR, str(e))
    