#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pip>=18.1',
    'bumpversion>=0.5.3',
    'wheel>=0.32.1',
    'watchdog>=0.9.0',
    'flake8>=3.5.0',
    'tox>=3.5.2',
    'coverage>=4.5.1',
    'Sphinx>=1.8.1',
    'twine>=1.12.1',
    'elasticsearch>=5.5.2',
    'elasticsearch-dsl>=5.4.0',
    'geoip2>=2.5.0',
    'pytz>=2017.3',
    'tzlocal>=1.4',
]

setup(
    author="Mozilla Infosec",
    author_email='infosec@mozilla.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Utilities shared throughout the MozDef codebase",
    install_requires=requirements,
    license='MPL-2.0',
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='mozdef_util',
    name='mozdef_util',
    packages=find_packages(),
    setup_requires=[],
    test_suite='tests',
    tests_require=[],
    url='https://github.com/mozilla/MozDef/tree/master/lib',
    version='1.0.7',
    zip_safe=False,
)
