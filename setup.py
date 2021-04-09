# -*- coding: utf-8 -*-
from __future__ import with_statement

import sys

from setuptools import setup, find_packages


# Do not change the variable name.  It's parsed by doc/conf.py script.
version = '0.1.7'

requires = ['Sphinx >= 1.2', 'six']


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='sphinxcontrib-autoprogram',
    version=version,
    url='https://github.com/sphinx-contrib/autoprogram',
    license='2-Clause BSD',
    author='Hong Minhee',
    author_email='\x68\x6f\x6e\x67.minhee' '@' '\x67\x6d\x61\x69\x6c.com',
    description='Documenting CLI programs',
    long_description=readme(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Topic :: Utilities'
    ],
    python_requires='>=3.7',
    platforms='any',
    packages=find_packages(),
    namespace_packages=['sphinxcontrib'],
    include_package_data=True,
    install_requires=requires,
    test_suite='sphinxcontrib.autoprogram.suite'
)
