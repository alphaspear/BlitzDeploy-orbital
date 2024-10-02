import socket
from sys import prefix

from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/")
def get_health():
    hostname = socket.gethostname()
    return f"App running in {hostname}"
