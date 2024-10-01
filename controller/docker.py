from service.docker import get_container_list, rename_container2
from fastapi import APIRouter
import json
# Define the router with a prefix
router = APIRouter(prefix="/docker", tags=["docker"])

@router.get("")
def get_health():
    return f"welcome to docker endpoint"

@router.get("/list")
def get_list():
    return json.dumps(get_container_list())

@router.patch("/rename/{oldname}")
def rename_container(oldname: str):
    rename_container2(oldname, "abhilash")
