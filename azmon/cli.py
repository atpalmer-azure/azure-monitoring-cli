from azure.mgmt.monitor import MonitorManagementClient
from azure.common.client_factory import get_client_from_cli_profile
import click
from .tools import jsontools, clicktools
from .config import ResourceConfig
from .core import Metrics, CosmosMetrics


@click.group()
@click.option('-c', '--config', default='./resources.config')
@click.pass_context
@clicktools.handle_errors
def main(ctx, config):
    ctx.obj = ResourceConfig.load_toml(config)


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


@cosmos.command()
@click.pass_obj
@clicktools.handle_errors
def rups(metrics_client):
    """Cosmos DB Request Units per Second"""
    result = metrics_client.ru_per_s()
    print(jsontools.dumps(result))


@cosmos.command()
@click.pass_obj
@clicktools.handle_errors
def ru(metrics_client):
    """Cosmos DB Request Units per Minute"""
    result = metrics_client.total_request_units()
    print(jsontools.dumps(result))
