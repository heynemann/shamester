#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from shamester_api import __version__

tests_require = [
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'honcho',
]

setup(
    name='shamester',
    version=__version__,
    description='Shamester is a service to track your website health.',
    long_description='''
Shamester is a service to track your website health.
''',
    keywords='seo health web',
    author='Globo.com',
    author_email='appdev@corp.globo.com',
    url='',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'cow-framework',
        'ujson',
        'motor',
        'toredis'
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            'shamester-api=shamester_api.server:main',
        ],
    },
)
