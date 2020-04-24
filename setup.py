# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')

setup(
    long_description=readme,
    name='layeredimage',
    version='2020.2.1',
    description='Use this module to read, and write to a number of layered image formats',
    python_requires='==3.*,>=3.6.0',
    project_urls={
        "documentation":
            "https://github.com/FHPythonUtils/LayeredImage/blob/master/README.md",
        "homepage":
            "https://github.com/FHPythonUtils/LayeredImage",
        "repository":
            "https://github.com/FHPythonUtils/LayeredImage"
    },
    author='FredHappyface',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent'
    ],
    packages=['LayeredImage'],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'defusedxml==0.*,>=0.6.0', 'gimpformats-unofficial==0.*,>=0.1.0',
        'metprint==2020.*,>=2020.5.0', 'numpy==1.*,>=1.18.3',
        'pillow==7.*,>=7.1.1', 'psd-tools3==1.*,>=1.8.2', 'pyora==0.*,>=0.3.0',
        'pypdn==1.*,>=1.0.3', 'scikit-image==0.*,>=0.16.2'
    ],
)
