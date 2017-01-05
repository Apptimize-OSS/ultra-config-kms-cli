"""
The cli command tool for this project.
This should include helpful, common commands for
the application.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import click

import ultra_config_kms_cli


@click.group()
def main(args=None):
    """Console script for ultra_config_kms_cli"""
    pass


@main.command()
def version():
    """
    Displays the version of ultra-config-kms-cli
    """
    click.echo(ultra_config_kms_cli)


if __name__ == "__main__":
    main()
