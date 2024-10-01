import docker

class DockerService:
    def __init__(self):
        self.client = docker.from_env()

    def get_containers(self):
        return self.client.containers.list()

def get_container_list():
    docker_service = DockerService()
    container_name_list = []
    for container in docker_service.get_containers():
        container_name_list.append(container.name)
    return container_name_list

def rename_container2(container_name, new_container_name):
    docker_service = DockerService()
    docker_service.client.containers.get(container_name).rename(new_container_name)