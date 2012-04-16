#!/usr/bin/env python

from distutils.core import setup

CLASSIFIERS = [
	"Development Status :: 5 - Production/Stable",
	"Intended Audience :: Developers",
	"License :: OSI Approved :: MIT License",
	"Programming Language :: Python",
]

import mfil
VERSION = mfil.__version__

setup(
	name = "python-mfil",
	py_modules = ["mfil"],
	author = "Jerome Leclanche",
	author_email = "jerome.leclanche@gmail.com",
	classifiers = CLASSIFIERS,
	description = "Battle.net Authenticator routines in Python.",
	download_url = "http://github.com/Adys/python-mfil/tarball/master",
	url = "http://github.com/Adys/python-mfil",
	version = VERSION,
)
