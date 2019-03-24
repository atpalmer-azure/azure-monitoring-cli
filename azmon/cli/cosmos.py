from ..tools import clicktools


def commands(group):
    @clicktools.metric_command(group)
    def requests(metrics_client, **kwargs):
        """Cosmos DB metadata requests"""
        return metrics_client.total_requests(**kwargs)

    @clicktools.metric_command(group)
    def metareq(metrics_client, **kwargs):
        """Cosmos DB metadata requests"""
        return metrics_client.metadata_requests(**kwargs)

    @clicktools.metric_command(group)
    def rups(metrics_client, **kwargs):
        """Cosmos DB Request Units per Second"""
        return metrics_client.ru_per_s(**kwargs)

    @clicktools.metric_command(group)
    def ru(metrics_client, **kwargs):
        """Cosmos DB Request Units per Minute"""
        return metrics_client.total_request_units(**kwargs)

    @clicktools.metric_command(group)
    def provisioned(metrics_client, **kwargs):
        """Cosmos DB provisioned RU/s throughput"""
        return metrics_client.provisioned_throughput(**kwargs)

    @clicktools.metric_command(group)
    def data(metrics_client, **kwargs):
        """Cosmos DB total data usage"""
        return metrics_client.data_usage(**kwargs)

    @clicktools.metric_command(group)
    def index(metrics_client, **kwargs):
        """Cosmos DB total data usage"""
        return metrics_client.index_usage(**kwargs)

    @clicktools.metric_command(group)
    def documents(metrics_client, **kwargs):
        """Cosmos DB document count"""
        return metrics_client.document_count(**kwargs)
