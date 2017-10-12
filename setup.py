from setuptools import setup, find_packages
import os

with open('LICENSE') as f:
    license = f.read()

setup(
  name = 'sphinx-bootstrap-directive',
  packages=find_packages(exclude=('tests', 'docs')),
  version = '0.1',
  url = 'http://sphinx-bootstrap-directives.readthedocs.io/',
  description = 'A library which allows you to bootstap elements in rst files',
)
