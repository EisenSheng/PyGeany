PyGeany
=======

About
----------
This small library provides you with a simple interface to open files in
an active geany instance. This can be used in simple Scripts for example.

Example
------------
Opening a file:

    >>> import PyGeany
    >>> with PyGeany.GeanyConnection() as a:
    ...     a.send_open('/tmp/test')
    ...
