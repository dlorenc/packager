from concurrent import futures

import grpc
import hashlib
import os

import service_pb2
import service_pb2_grpc
import sys


def main():
  channel = grpc.insecure_channel('localhost:50051')
  stub = service_pb2_grpc.AppBuilderStub(channel)

  # Create Container
  # pj = open('package.json', 'r').read()
  # pl = open('package-lock.json', 'r').read()
  # stub.BuildContainer(service_pb2.BuildContainerRequest(
  #   base_image='gcr.io/google-appengine/nodejs:latest',
  #   destination_image='gcr.io/dlorenc-vmtest2/foobartest:latest',
  #   npm_config=service_pb2.NpmConfig(package_json=pj, package_lock_json=pl))
  # )

  rt = open('requirements.txt', 'r').read()
  stub.BuildContainer(service_pb2.BuildContainerRequest(
    base_image='gcr.io/google-appengine/python:latest',
    destination_image='gcr.io/dlorenc-vmtest2/foobartestpy:latest',
    pip_config=service_pb2.PipConfig(requirements_txt=rt))
  )


if __name__ == '__main__':
  main()