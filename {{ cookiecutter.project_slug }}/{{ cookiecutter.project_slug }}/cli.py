#!/usr/bin/env python

import click


@click.group()
@click.version_option(version={{cookiecutter.project_slug}}.__version__)
def entry_point():
    pass
