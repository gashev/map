#!/usr/bin/python
# coding=utf-8
"""
Setuptools setup file, used to install or test 'map'
"""
import sys
from setuptools import setup

VERSION = '0.1'
DESCRIPTION = "map - paths mapping."
LONG_DESCRIPTION = "map - paths mapping."

CLASSIFIERS = list(filter(None, map(str.strip,
"""
Development Status :: 1 - Planning
Environment :: Console
Operating System :: OS Independent
Intended Audience :: Developers
Intended Audience :: System Administrators
License :: OSI Approved :: GNU General Public License v3 (GPLv3)
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: Implementation :: CPython
Programming Language :: Python :: Implementation :: PyPy
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines())))

INSTALL_REQUIRES = []

setup(
    name="map",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    author='Oleg Gashev',
    author_email='oleg@gashev.net',
    url='https://github.com/gashev/map',
    license='GPL-3',
    platforms=['any'],
    py_modules=["map"],
    keywords='paths mapping',
    install_requires=INSTALL_REQUIRES,
    scripts=['bin/map', 'bin/map.sh']
)

