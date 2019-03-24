from azure.mgmt.monitor import MonitorManagementClient
from azure.common.client_factory import get_client_from_cli_profile
import click
from ..tools import clicktools
from ..config import ResourceConfig
from ..metrics import Metrics, CosmosMetrics
from .cosmos import commands as cosmos_commands


@click.group()
@click.option('-c', '--config', default='./resources.config')
@click.pass_context
@clicktools.handle_errors
def main(ctx, config):
    ctx.obj = ResourceConfig.load_toml(config)


@clicktools.subcommands(cosmos_commands)
@main.group()
@click.argument('environment')
@click.argument('resource')
@click.pass_context
@clicktools.handle_errors
def cosmos(ctx, environment, resource):
    """Cosmos DB commands"""
    resource_id = ctx.obj.get_resource(environment, resource)
    ctx.obj = Metrics.create_interface(
        client=get_client_from_cli_profile(MonitorManagementClient),
        resource_id=resource_id,
        interface=CosmosMetrics,
    )
