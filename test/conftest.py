from __future__ import print_function
import os
import platform
import site
import shutil


# This is a hack! TODO explain (if it works) XXX
if 'CIBUILDWHEEL' in os.environ and platform.system().startswith('Windows'):
    site_packages = site.getsitepackages()[1]
    dirname = os.path.dirname(__file__)
    dll = os.path.join(dirname, '..', 'windows', 'admesh', 'libadmesh-1.dll')
    shutil.copy(dll, site_packages)
    print('Copying', dll, 'to', site_packages)
