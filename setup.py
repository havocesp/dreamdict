#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# if sys.version_info < (3, 5):
#     raise NotImplementedError("Sorry, you need at least Python 2.6 or Python 3.2+ to use py-term.")

import dreamdict as dd

setup(name=dd.__project__,
      version=dd.__version__,
      description=dd.__description__,
      long_description=dd.__description__,
      author=dd.__author__,
      author_email=dd.__email__,
      url=dd.__site__,
      py_modules=[dd.__package__],
      license=dd.__license__,
      platforms=dd.__platforms__,
      keywords=dd.__keywords__,
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Development Status :: 5 - Production/Stable'
      ],
      )
