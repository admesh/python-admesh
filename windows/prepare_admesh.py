from __future__ import print_function
import io
import os
import requests
import shutil
import sys
import zipfile


VERSION = '0.98.3'
ARCH = 64 if sys.maxsize > 2**32 else 32

# AppVeyor hack
# When this is run, it is (currently) with 32bit Python
# However, we need it to be the same as Pythons that will build the wheels
# On AppVeyor, we run twice, once with CIBW_SKIP to skip 64b wheels, later 32b,
if 'CIBW_SKIP' in os.environ:
    ARCH = 64 if os.environ['CIBW_SKIP'].endswith('32') else 32


DIRNAME = 'admesh-win{arch}-{version}'.format(arch=ARCH, version=VERSION)

URL = ('https://github.com/admesh/admesh/releases/download/v{version}/'
       '{dirname}.zip').format(version=VERSION, dirname=DIRNAME)


def download_unpack():
    response = requests.get(URL, stream=True)
    with zipfile.ZipFile(io.BytesIO(response.content), 'r') as admeshzip:
        admeshzip.extractall()


def move():
    dst = 'windows/admesh'
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.move(DIRNAME, dst)

    # mingw names it .dll.a, but python expects .lib
    shutil.move(dst + '/lib/libadmesh.dll.a',
                dst + '/lib/libadmesh.lib')


if __name__ == '__main__':
    print('Downloading', URL)
    download_unpack()
    move()
