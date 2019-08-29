#!/usr/bin/python
# coding=UTF-8
'''
@Author: Recar
@Date: 2019-08-29 17:37:08
@LastEditTime: 2019-08-29 17:55:58
'''
import click
from app.utils.invitationcode_util import generate_admin

@click.group()
def cli():
    pass

@click.command("admin")
def admin():
    click.echo("create admin")
    generate_admin()

cli.add_command(admin)

if __name__ == "__main__":
    cli()