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
    version='2020.6.4',
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
        'Environment :: Console', 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers', 'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License', 'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    packages=['LayeredImage'],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'blendmodes==2020.*,>=2020.2.2', 'defusedxml==0.*,>=0.6.0',
        'gimpformats==2020.*,>=2020.2.3', 'metprint==2020.*,>=2020.6.1',
        'numpy==1.*,>=1.18.4', 'pillow==7.*,>=7.1.2', 'psd-tools3==1.*,>=1.8.2',
        'pylsr==2020.*,>=2020.0.3', 'pyora==0.*,>=0.3.8', 'pypdn==1.*,>=1.0.5'
    ],
    extras_require={"dev": ["imgcompare==2.*,>=2.0.1"]},
)
