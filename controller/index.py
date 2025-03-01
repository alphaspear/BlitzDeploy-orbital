import socket
from sys import prefix

from fastapi import APIRouter

router = APIRouter(tags=["home"])

@router.get("/")
def home():
    return "BlitzDeploy Orbital API interface";
