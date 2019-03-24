import os
from setuptools import setup, find_packages


setup(
    name='azmon',
    author='A. Palmer',
    author_email='andrew.t.palmer@parker.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [ 'azmon=azmon.cli:main' ],
    },
    install_requires=[
        'azure-mgmt-monitor',
        'azure-cli-core',
        'toml',
        'click',
        'crayons',
    ],
    package_data={ '': [ 'data/*'] },
)
