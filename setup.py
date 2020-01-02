# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: henry
# Created Time: 2020/1/2 10:54

from setuptools import setup
import os

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
try:
    readme = f.read()
    f.close()
except Exception:
    readme = "pytimelib is a simple model for python to do time conversion."

setup(
    name='pytimelib',
    description='pytimelib is a simple model for python to do time conversion.',
    long_description=readme,
    author='henry_czh',
    author_email='henry_czh@foxmail.com',
    url='https://github.com/Geoge-Henry/timelib-py',
    version=__import__('pytimelib').__version__,
    packages=['pytimelib'],
    include_package_data=True,
    install_requires=[],
)
