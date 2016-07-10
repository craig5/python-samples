#!/usr/bin/env python
"""Setup for simple, single script app."""
from __future__ import print_function
import setuptools


setup_args = {
    'name': 'single_script',
    'version': '0.0.1',
    'description': 'Example with a single script.',
    'author': 'Craig Sebenik',
    'author_email': 'craig@users.noreply.github.com',
}


_LIB_DIR = 'lib'
setup_args['package_dir'] = {'': _LIB_DIR}
setup_args['packages'] = setuptools.find_packages(_LIB_DIR)
setup_args['entry_points'] = {
    'console_scripts': ['single-simple = single_script.scripts:simple']
}


setuptools.setup(**setup_args)
# End of file.
