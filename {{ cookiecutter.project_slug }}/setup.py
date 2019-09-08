#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

# core modules
from setuptools import find_packages
from setuptools import setup
import io
import os
import unittest

# internal modules
exec(open("{{ cookiecutter.project_slug }}/_version.py").read())


def read(file_name):
    """Read a text file and return the content as a string."""
    with io.open(os.path.join(os.path.dirname(__file__), file_name),
                 encoding="utf-8") as f:
        return f.read()


def my_test_suite():
    """Return a a composite test consisting of a number of TestCases."""
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("tests", pattern="test_*.py")
    return test_suite


config = {
    "name": "{{ cookiecutter.project_slug }}",
    "version": __version__,
    "author": '{{ cookiecutter.full_name.replace("\"", "\\\"") }}',
    "author_email": "{{ cookiecutter.email }}",
    "maintainer": '{{ cookiecutter.full_name.replace("\"", "\\\"") }}',
    "maintainer_email": "{{ cookiecutter.email }}",
    "packages": find_packages(),
    "entry_points": {
        "console_scripts": ["clana={{ cookiecutter.project_slug }}.cli:entry_point"]
    },
    "platforms": ["Linux"],
    "url": "",  # TODO
    "download_url": "",  # TODO
    "license": "{{ cookiecutter.open_source_license }}",
    "description": '{{ cookiecutter.project_short_description.replace("\'", "\\\'") }}',
    "long_description": read("README.md"),
    "long_description_content_type": "text/markdown",
    "install_requires": ["click"],
    "keywords": ["utility"],
    # TODO:
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    "classifiers": [
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
    ],
    "zip_safe": False,
    "test_suite": "setup.my_test_suite",
}

setup(**config)
