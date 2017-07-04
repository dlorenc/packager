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


def handle_app(pm, base_image, cache_dir):
    packages = pm.get_package_list()
    img = base_image
    # This loop could be parallelized.
    for pkg in packages:
        contents = get_layer_cache(pkg, cache_dir)
        if not contents:
            contents = pm.build_layer_for_one_package(pkg)
            set_layer_cache(pkg, contents, cache_dir)
            img = append.Layer(img, contents)
    return img


class NPM(object):
    def __init__(self, npm_config):
        self.package_json_contents = json.loads(npm_config.package_json)
        self.package_lock_contents = json.loads(npm_config.package_lock_json)

    def get_package_list(self):
        deps = []
        for name in self.package_json_contents['dependencies']:
            version = self.package_lock_contents['dependencies'][name]['version']
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
