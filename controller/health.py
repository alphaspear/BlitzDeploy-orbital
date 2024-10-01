import socket
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def get_health():
    hostname = socket.gethostname()
    return f"App running in {hostname}"
