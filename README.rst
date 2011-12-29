PyGeany
=======

About
----------
This small library provides you with a simple interface to open files in
an active geany instance. This can be used in simple scripts for example.


Requirements
-----------------
This library depends on PyGObject. Unfortunately I can't specify this in the
``setup.py`` file because as of version 2.28.3 PyGObject doesn't support the
installation process with pip. This is an issue but I can't help it.


Example
------------
Opening a file:

    >>> import PyGeany
    >>> with PyGeany.GeanyConnection() as a:
    ...     a.send_open('/tmp/test')
    ...
