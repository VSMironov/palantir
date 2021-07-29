# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='palantir',
    version='0.1.0',
    description='Sample package for grabber picture',
    long_description=readme,
    author='Vitaliy Mironov',
    author_email='me@vsmironov.ru',
    url='https://github.com/VSMironov/palantir',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'venv'))
)
