#!/usr/bin/env python

# Third party modules
import click

# First party modules
import {{cookiecutter.project_slug}}


@click.group()
@click.version_option(version={{cookiecutter.project_slug}}.__version__)
def entry_point():
    """Awesomeproject spreads pure awesomeness."""
