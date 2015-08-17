# -*- coding: utf-8 -*-
from __future__ import with_statement

import sys

from setuptools import setup, find_packages


# Do not change the variable name.  It's parsed by doc/conf.py script.
version = '0.1.2'

requires = ['Sphinx >= 1.2', 'six']

if sys.version_info < (2, 7):
    requires.append('argparse')


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='sphinxcontrib-autoprogram',
    version=version,
    url='https://bitbucket.org/birkenfeld/sphinx-contrib',
    license='BSD',
    author='Hong Minhee',
    author_email='minhee' '@' 'dahlia.kr',
    description='Documenting CLI programs',
    long_description=readme(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Topic :: Utilities'
    ],
    platforms='any',
    packages=find_packages(),
    namespace_packages=['sphinxcontrib'],
    include_package_data=True,
    test_suite='sphinxcontrib.autoprogram.suite',
    install_requires=requires
)
