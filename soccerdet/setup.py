#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='soccerdet',
    version='0.1',
    packages=find_packages(),
    scripts=['manage.py'],
    url='https://github.com/neoaggelos/soccerdet',
    author='Aggelos Kolaitis',
    install_requires=[
        'django',
        'dj-database-url',
        'psycopg2',
        'pyyaml',
    ],
    include_package_data=True
)
