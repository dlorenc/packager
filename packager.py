import base64
import cStringIO
import httplib2
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time

from containerregistry.client import docker_creds
from containerregistry.client import docker_name
from containerregistry.client.v2_2 import append
from containerregistry.client.v2_2 import docker_image
from containerregistry.client.v2_2 import docker_session
from containerregistry.client.v2_2 import save
from containerregistry.transport import transport_pool


IMAGE = 'gcr.io/google-appengine/nodejs:latest'


def get_layer_cache(pkg, cache_dir):
    pkg_path = os.path.join(cache_dir, base64.b64encode(pkg))
    if os.path.exists(pkg_path):
        with open(pkg_path, 'rb') as f:
            return f.read()
    return False


def set_layer_cache(pkg, contents, cache_dir):
    pkg_path = os.path.join(cache_dir, base64.b64encode(pkg))
    with open(pkg_path, 'wb') as f:
        f.write(contents)


def handle_app(pm, cache_dir):
    packages = pm.get_package_list()
    img = pm.base_image()
    # This loop could be parallelized.
    for pkg in packages:
        contents = get_layer_cache(pkg, cache_dir)
        if not contents:
            contents = pm.build_layer_for_one_package(pkg)
            set_layer_cache(pkg, contents, cache_dir)
            img = append.Layer(img, contents)
    return img


def main(root_dir, dst_image):
    transport = transport_pool.Http(httplib2.Http, size=32)
    cache_dir = os.path.join(root_dir, '.cache')
    if not os.path.exists(cache_dir):
        os.makedirs(cache_dir)
    base = docker_name.Tag('gcr.io/google-appengine/nodejs:latest')
    creds = docker_creds.DefaultKeychain.Resolve(base)        
    with docker_image.FromRegistry(base, creds, transport) as base_img:
        npm = NPM(root_dir, base_img)
        for i in range(10):
            start = time.time()
            dst = docker_name.Tag(dst_image)
            creds = docker_creds.DefaultKeychain.Resolve(dst)
            with docker_session.Push(dst, creds, transport, threads=32) as session:
                img = handle_app(npm, cache_dir)
                session.upload(img)
            print time.time() - start


class NPM(object):
    
    def __init__(self, app_dir, base_img):
        self._app_dir = app_dir
        self._base = base_img
        # Force it to load everything.
        self._base.manifest()

    def base_image(self):
        return self._base

    def get_package_list(self):
        pj = os.path.join(self._app_dir, 'package.json')
        with open(pj) as f:
            package_contents = json.load(f)
        
        pl = os.path.join(self._app_dir, 'package-lock.json')
        with open(pl) as f:
            package_lock_contents = json.load(f)

        deps = []
        for name in package_contents['dependencies']:
            version = package_lock_contents['dependencies'][name]['version']
            deps.append('%s@%s' % (name, version))
        return deps

    def build_layer_for_one_package(self, pkg):
        script = """\
npm install %s --global-style
tar -czf /tmp/node_modules/node_modules.tar.gz /app/node_modules
chmod -R +r /tmp/node_modules
        """ % pkg

        try:
            tmp_path = tempfile.mkdtemp(dir='/tmp')
            subprocess.check_call(['docker', 'run', '-v', '%s:%s' % (tmp_path, '/tmp/node_modules'), '--rm', IMAGE, 'sh', '-c', script])
            with open(os.path.join(tmp_path, 'node_modules.tar.gz')) as f:
                contents = f.read()
        finally:
            shutil.rmtree(tmp_path)
        return contents


if __name__ == "__main__":
    # Root dir is the first arg.
    if len(sys.argv) != 3:
        print 'Usage: bazel run :packager -- $(pwd) <IMAGE_NAME>'
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
