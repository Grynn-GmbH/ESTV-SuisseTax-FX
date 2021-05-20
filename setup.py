# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in estv_suissetax_fx/__init__.py
from estv_suissetax_fx import __version__ as version

setup(
	name='estv_suissetax_fx',
	version=version,
	description='Sync Your FX Rates',
	author='Grynn GMBH',
	author_email='grynn@in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
