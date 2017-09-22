from __future__ import print_function
import glob
import sys
import zipfile


DLL = 'libadmesh-1.dll'
DLLPATH = 'windows/admesh/' + DLL


def inject_into(wheelpath):
    with zipfile.ZipFile(wheelpath, 'a') as wheel:
        wheel.write(DLLPATH, DLL)


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        for path in glob.glob(arg):
            print('Injecting the admesh dll into', path)
            inject_into(path)
