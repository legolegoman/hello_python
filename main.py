import docker
client = docker.from_env()

#for container in client.containers.list():
#  print container.id


print client.containers.run('busybox', 'bin/echo hello', remove=True)
