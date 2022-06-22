#!/usr/bin/env python
# coding: utf-8

from setuptools import find_packages, setup


setup(
    name='trees-everywhere',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='trees-everywhere',
    url='https://github.com/HenriqueLR/trees-everywhere',
    author='Henrique Luz Rodrigues',
    author_email='henrique.lr89@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',                                
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
