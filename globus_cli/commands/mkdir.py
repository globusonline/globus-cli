import click

from globus_cli.parsing import ENDPOINT_PLUS_REQPATH, command
from globus_cli.safeio import FORMAT_TEXT_RAW, formatted_print
from globus_cli.services.transfer import autoactivate, get_client


@command("mkdir")
@click.argument("endpoint_plus_path", type=ENDPOINT_PLUS_REQPATH)
def mkdir_command(endpoint_plus_path):
    """Make a directory on an endpoint"""
    endpoint_id, path = endpoint_plus_path

    client = get_client()
    autoactivate(client, endpoint_id, if_expires_in=60)

    res = client.operation_mkdir(endpoint_id, path=path)
    formatted_print(res, text_format=FORMAT_TEXT_RAW, response_key="message")
