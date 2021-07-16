import click
from clients import commands as clients_commands

CLIENTS_TABLE = '.clients.csv'

@click.group()
@click.pass_context
def cli(ctx):
    """
    This is the entry point of the application
    using the application's context object (ctx)
    """
    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENTS_TABLE


cli.add_command(clients_commands.all)

