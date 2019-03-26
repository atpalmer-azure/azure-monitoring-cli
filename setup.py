import os
from setuptools import setup, find_packages
from time import time


CONFIG_INSTALL_PATH = os.path.abspath(os.path.join(os.getenv('HOME', os.path.curdir), '.azmon'))


setup(
    name='azmon',
    version=int(time()),
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
    data_files=[
        (CONFIG_INSTALL_PATH, [ './config/resources.cfg' ]),
    ],
)
