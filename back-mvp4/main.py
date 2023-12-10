from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from entities import machine, Session
# from dtos.request import MachineReqModel

from controllers.machine_controller import include_route as machine_controller

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


machine_controller(app)