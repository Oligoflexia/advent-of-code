from setuptools import setup, find_packages

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

setup(
    name='advent-of-code',
    version='0.1',
    packages=find_packages(),
    install_requires=reqs,
)