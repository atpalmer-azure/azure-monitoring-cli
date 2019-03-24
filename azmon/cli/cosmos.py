import click
from ..tools import jsontools, clicktools


def commands(cosmos):
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


    @cosmos.command()
    @click.pass_obj
    @clicktools.handle_errors
    def data(metrics_client):
        """Cosmos DB total data usage"""
        result = metrics_client.data_usage()
        print(jsontools.dumps(result))


    @cosmos.command()
    @click.pass_obj
    @clicktools.handle_errors
    def count(metrics_client):
        result = metrics_client.document_count()
        print(jsontools.dumps(result))
