from setuptools import setup, find_packages

setup(
    name='mtgsim',
    version='0.0.1',
    author='Will',
    author_email='',
    description='Simulator for magic the gathering draw/deck stats',
    packages=find_packages(),
    install_requires=[
        'jupyter',
    ],
)
