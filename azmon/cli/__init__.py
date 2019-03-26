import os
from azure.mgmt.monitor import MonitorManagementClient
from azure.common.client_factory import get_client_from_cli_profile
import click
from ..tools import clicktools
from ..config import ResourceConfig
from ..metrics import Metrics, CosmosMetrics, IotHubMetrics, SqlMetrics
from .cosmos import commands as cosmos_commands
from .iothub import commands as iothub_commands
from .sql import commands as sql_commands


DEFAULT_CONFIG = os.path.abspath(os.path.join(os.getenv('HOME', os.path.curdir), '.azmon', 'resources.cfg'))


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


@clicktools.subcommands(iothub_commands)
@main.group()
@click.argument('environment')
@click.argument('resource')
@click.pass_context
@clicktools.handle_errors
def iothub(ctx, environment, resource):
    """IoT Hub commands"""
    resource_id = ctx.obj.get_resource(environment, resource)
    ctx.obj = Metrics.create_interface(
        client=get_client_from_cli_profile(MonitorManagementClient),
        resource_id=resource_id,
        interface=IotHubMetrics,
    )


@clicktools.subcommands(sql_commands)
@main.group()
@click.argument('environment')
@click.argument('resource')
@click.pass_context
@clicktools.handle_errors
def sql(ctx, environment, resource):
    """Microsoft SQL Server commands"""
    resource_id = ctx.obj.get_resource(environment, resource)
    ctx.obj = Metrics.create_interface(
        client=get_client_from_cli_profile(MonitorManagementClient),
        resource_id=resource_id,
        interface=SqlMetrics,
    )
