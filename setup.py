from pkg_resources import parse_requirements
from setuptools import setup

install_reqs = parse_requirements('requirements.txt')

setup(
    name='module6_automated_testing',
    version='1.0.0',
    author_email='baumgar2@canisius.edu',
    author='Kyle Baumgardner',
    packages=['cyb600_module6'],
    tests=['tests'],
    license='Apache License Version 2.0',
)