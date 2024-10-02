from service.docker import get_container_list, container_rename, get_container_info
from fastapi import APIRouter
import json
# Define the router with a prefix
router = APIRouter(prefix="/docker", tags=["docker"])

# @router.get("")
# def get_health():
#     return f"welcome to docker endpoint"

@router.get("/")
def get_container_by_id(id: str):
    try:
        return get_container_info(id)
    except Exception as e:
        return str(e)


@router.get("/list")
def get_list():
    try:
        resp = get_container_list()
        return resp
    except Exception as e:
        return str(e)


@router.patch("/rename")
def rename_container(old_name: str = None, new_name: str = None):
    container_rename(old_name, new_name)

