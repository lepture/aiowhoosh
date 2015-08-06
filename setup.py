#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup


def fread(filename):
    with open(filename) as f:
        return f.read()


setup(
    name='aiowhoosh',
    version='0.1',
    author='Hsiaoming Yang',
    author_email='me@lepture.com',
    url='https://github.com/lepture/aiowhoosh',
    packages=[
        "aiowhoosh",
    ],
    description="Whoosh HTTP Server with aiohttp",
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    long_description=fread('README.rst'),
    license='BSD',
    install_requires=[
        'Whoosh',
        'aiohttp',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
