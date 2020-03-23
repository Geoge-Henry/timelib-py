# !/usr/bin/python
# -*- coding:utf-8 -*-
# Author: henry
# Created Time: 2020/1/2 10:54

from setuptools import setup
import os


root_directory = os.path.abspath(os.path.dirname(__file__))


# 读取文件内容
def read_file(filename):
    with open(os.path.join(root_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


setup(
    name='pytimelib',
    description='pytimelib is a simple model for python to do time conversion.',
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    author='henry_czh',
    author_email='henry_czh@foxmail.com',
    url='https://github.com/Geoge-Henry/timelib-py',
    version=__import__('pytimelib').__version__,
    packages=['pytimelib'],
    include_package_data=True,
    install_requires=read_requirements('requirements.txt'),
)
