import docker
from models.models import ContainerInfo

class DockerService:
    def __init__(self):
        self.client = docker.from_env()

    def get_containers(self):
        return self.client.containers.list()

    def get_container(self, container_id):
        return self.client.containers.get(container_id)

def get_container_list():
    docker_service = DockerService()
    container_list = []
    for container in docker_service.get_containers():
        container_info = ContainerInfo(
            id=container.id,
            name=container.name,
            image=container.image.tags[0] if container.image.tags else "unknown",
            status=container.status
        )
        container_list.append(container_info)
    return container_list

def get_container_info(id):
    docker_service = DockerService()
    container = docker_service.get_container(id)
    container_info = ContainerInfo(
        id=container.id,
        name=container.name,
        image=container.image.tags[0] if container.image.tags else "unknown",
        status=container.status
    )
    return container_info

def container_rename(container_name, new_container_name):
    docker_service = DockerService()
    docker_service.client.containers.get(container_name).rename(new_container_name)