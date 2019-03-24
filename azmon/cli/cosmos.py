import click
from ..tools import clicktools


def commands(group):
    @group.command()
    @click.option('-c', '--count', default=1)
    @click.pass_obj
    @clicktools.handle_result
    def requests(metrics_client, **kwargs):
        """Cosmos DB metadata requests"""
        return metrics_client.total_requests(**kwargs)

    @group.command()
    @click.option('-c', '--count', default=1)
    @click.pass_obj
    @clicktools.handle_result
    def metareq(metrics_client, **kwargs):
        """Cosmos DB metadata requests"""
        return metrics_client.metadata_requests(**kwargs)

    @group.command()
    @click.option('-c', '--count', default=1)
    @click.pass_obj
    @clicktools.handle_result
    def rups(metrics_client, **kwargs):
        """Cosmos DB Request Units per Second"""
        return metrics_client.ru_per_s(**kwargs)

    @group.command()
    @click.option('-c', '--count', default=1)
    @click.pass_obj
    @clicktools.handle_result
    def ru(metrics_client, **kwargs):
        """Cosmos DB Request Units per Minute"""
        return metrics_client.total_request_units(**kwargs)

    @group.command()
    @click.option('-c', '--count', default=1)
    @click.pass_obj
    @clicktools.handle_result
    def provisioned(metrics_client, **kwargs):
        """Cosmos DB provisioned RU/s throughput"""
        return metrics_client.provisioned_throughput(**kwargs)

    @group.command()
    @click.option('-c', '--count', default=1)
    @click.pass_obj
    @clicktools.handle_result
    def data(metrics_client, **kwargs):
        """Cosmos DB total data usage"""
        return metrics_client.data_usage(**kwargs)

    @group.command()
    @click.option('-c', '--count', default=1)
    @click.pass_obj
    @clicktools.handle_result
    def index(metrics_client, **kwargs):
        """Cosmos DB total data usage"""
        return metrics_client.index_usage(**kwargs)

    @group.command()
    @click.option('-c', '--count', default=1)
    @click.pass_obj
    @clicktools.handle_result
    def documents(metrics_client, **kwargs):
        """Cosmos DB document count"""
        return metrics_client.document_count(**kwargs)
