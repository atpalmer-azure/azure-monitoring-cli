import os
from azure.mgmt.monitor import MonitorManagementClient
from azure.common.client_factory import get_client_from_cli_profile
import click
from ..tools import clicktools
from ..config import ResourceConfig
from ..metrics import Metrics, CosmosMetrics
from .cosmos import commands as cosmos_commands


DEFAULT_CONFIG = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'data', 'resources.config'))


@click.group()
@click.option('-c', '--config', default=DEFAULT_CONFIG, envvar='AZMON_RESOURCES_CONFIG_PATH')
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
