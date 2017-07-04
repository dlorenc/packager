from concurrent import futures
import cStringIO
import tarfile
import time

import grpc
import hashlib
import httplib2
import os

import service_pb2
import service_pb2_grpc

import packager

from containerregistry.client import docker_creds
from containerregistry.client import docker_name
from containerregistry.client.v2_2 import docker_image
from containerregistry.client.v2_2 import docker_session
from containerregistry.transport import transport_pool

class AppBuilderServicer(service_pb2.AppBuilderServicer):

    def __init__(self, cache_dir):
        self._cache_dir = cache_dir
        self._upload_dir = os.path.join(self._cache_dir, 'uploads')
        self._build_cache_dir = os.path.join(self._cache_dir, 'builds')
        self._base_image_cache = {}

        self.transport = transport_pool.Http(httplib2.Http, size=32)
        self.creds = docker_creds.DefaultKeychain.Resolve(docker_name.Registry('gcr.io'))

    def BuildContainer(self, request, context):
        # load base image
        if request.base_image not in self._base_image_cache:
            tag = docker_name.Tag(request.base_image)
            with docker_image.FromRegistry(tag, self.creds, self.transport) as base_image:
                self._base_image_cache[request.base_image] = base_image
        base_image = self._base_image_cache[request.base_image]

        which = request.WhichOneof("package_manager") 
        if which == "npm_config":
            pm = packager.NPM(request.npm_config)
        elif which == "pip":
            pass
            #pm = packager.PIP(request.pip_config)

        img = packager.handle_app(pm, base_image, self._build_cache_dir)
        dst = docker_name.Tag(request.destination_image)
        creds = docker_creds.DefaultKeychain.Resolve(dst)
        with docker_session.Push(dst, creds, self.transport, threads=32) as session:
            session.upload(img)
        return service_pb2.BuildContainerResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_AppBuilderServicer_to_server(
        AppBuilderServicer('.cache'), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()