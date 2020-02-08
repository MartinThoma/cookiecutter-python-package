#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `{{ cookiecutter.project_slug }}` package."""

# Third party modules
import pytest

# First party modules
import {{ cookiecutter.project_slug }}


def test_version():
    assert {{ cookiecutter.project_slug }}.__version__.count(".") == 2


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
