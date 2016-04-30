ADMesh bindings for Python
==========================

.. image:: https://badge.fury.io/py/admesh.svg
    :target: http://badge.fury.io/py/admesh

.. image:: https://travis-ci.org/admesh/python-admesh.png?branch=master
        :target: https://travis-ci.org/admesh/python-admesh

.. image:: https://pypip.in/d/admesh/badge.png
        :target: https://pypi.python.org/pypi/admesh

This module provides bindings for the `ADMesh <https://github.com/admesh/admesh>`_ library. It lets you manipulate 3D models in binary or ASCII STL format and partially repair them if necessary.

Installation
------------

First, you'll need to install the `ADMesh <https://github.com/admesh/admesh>`_ library. This release is designed for ADMesh 0.98.x. Follow the instructions there. Then you can install this as usual with **one** of the following:

.. code:: sh

    ./setup.py install
    python3 setup.py install # for Python 3
    pip install admesh # install directly from PyPI

In case your ADMesh library is located in non-standard location, you'll have to tell the compiler and linker where to look:

.. code:: sh

    LDFLAGS='-L/path/to/library' CFLAGS='-I/path/to/header' ./setup.py install

Usage
-----

Use the ``Stl`` class provided.

.. code:: python

    import admesh
    
    # load an STL file
    stl = admesh.Stl('file.stl')
    
    # observe the available methods
    help(stl)
    
    # read the stats
    stl.stats
    
    # see how many facets are there
    len(stl)
    
    # walk the facets
    for facet in stl:
        # get the normal
        facet['normal']
        # walk the vertices
        for vertex in facet['vertex']:
            # read the coordinates
            vertex['x']
            vertex['y']
            vertex['z']

Note that all C ADMesh functions start with ``stl_`` prefix and the Python methods of this module do not. Also note that not all C ADMesh functions are provided, because some would require more complicated approach and are not considered worthy. In case you are missing some functions, create `new issue <https://github.com/admesh/python-admesh/issues/new>`_.
