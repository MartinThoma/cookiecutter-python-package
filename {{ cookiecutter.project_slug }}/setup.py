#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

# core modules
from setuptools import setup

setup(
    entry_points={
        "console_scripts": ["clana={{ cookiecutter.project_slug }}.cli:entry_point"]
    },
    install_requires=["click"],
)
