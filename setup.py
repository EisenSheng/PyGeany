# -*- coding: utf-8 -*-

import sys

from setuptools import setup, find_packages


extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

setup(
    name='PyGeany',
    version='0.1',
    description="Provides support for geany's control socket",
    url='https://github.com/EisenSheng/PyGeany',
    classifiers=[
        'Development Status :: 0.1 - Alpha',
        'License :: Public Domain',
        'Topic :: Software Development :: Libraries'
    ],

    py_modules=['PyGeany'],
    zip_safe=True,
    install_requires=['distribute'],

    author='Arthur S.',
    author_email='arthur.s@redsmile.org',

    long_description="""
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

""",

    **extra
)
