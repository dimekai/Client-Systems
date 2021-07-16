import click

from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """
    Manages the clients lifecycle to define client's membership group
    @click.group converts to 'clients' function in other decorator
    """
    pass


@clients.command()
@click.option('-n', '--name',
        type=str,
        prompt=True,
        help='Specify the client name'
        )
@click.option('-c', '--company',
        type=str,
        prompt=True,
        help='Specify the client company'
        )
@click.option('-e', '--email',
        type=str,
        prompt=True,
        help='Specify the client email'
        )
@click.option('-p', '--position',
        type=str,
        prompt=True,
        help='Specify the client position'
        )
@click.pass_context
def create(ctx, name:str, company:str, email:str, position:str):
    """
    Creates a new client for sales-system

    Parameters
    ----------
    ctx : dict
        - Define the context of the application
          It is a empty dictionary
    """
    client_service = ClientService(ctx.obj['clients_table'])
    client = Client(name, company, email, position)

    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """
    Lists all clients of the sales-system
    """
    client_service = ClientService(ctx.obj['clients_table'])
    clients_list = client_service.list_clients()
    
    click.echo("  ID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION  |")
    click.echo("="*115)

    for client in clients_list:
        click.echo("{uid} | {name} | {company} | {email} | {position} |"
                .format(uid = client['uid']
                     , name = client['name']
                     , company = client['company']
                     , email = client['email']
                     , position = client['position']
                )
        )


@clients.command()
@click.argument('client_uid'
        , type=str
        )
@click.pass_context
def update(ctx, client_uid:str):
    """ 
    Updates a client of the sales-system
    """
    client_service = ClientService(ctx.obj['clients_table'])
    clients_list = client_service.list_clients()
    
    # Searching the client to modify
    client = [client for client in clients_list if client['uid'] == client_uid]

    if client:
        # We do a flow updating - Unpackage our client using **
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)

        click.echo('Client was updated')

    else:
        click.echo('Client not found')

    
@clients.command()
@click.argument('client_uid'
        , type=str
        )
@click.pass_context
def delete(ctx, client_uid:str):
    """
    Deletes a client of the sales-system
    """
    client_service = ClientService(ctx.obj['clients_table'])
    clients_list = client_service.list_clients()

    # Searching the cliento to be deleted
    client = [client for client in clients_list if client['uid'] == client_uid]

    if client:
        client_service.delete_client(client)
        click.echo('Client was deleted')
    else:
        click.echo('Client not found')


def _update_client_flow(client:Client):
    click.echo("=" * 75)
    click.echo("\tLeave empty if you don't want to modify the value")
    click.echo("=" * 75)

    # We are going to set the updated data
    client.name = click.prompt('New client name ', type=str, default=client.name)
    client.company = click.prompt('New client company ', type=str, default=client.company)
    client.email = click.prompt('New client email ', type=str, default=client.email)
    client.position = click.prompt('New client position ', type=str, default=client.position)
    
    return client


# Declare an alias to point to the 'clients' function
all = clients

