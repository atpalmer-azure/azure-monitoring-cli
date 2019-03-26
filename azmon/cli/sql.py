from ..tools import clicktools


def commands(group):
    @clicktools.metric_command(group)
    def cpu(metrics_client, **kwargs):
        """CPU percentage"""
        return metrics_client.cpu_percent(**kwargs)

    @clicktools.metric_command(group)
    def dataio(metrics_client, **kwargs):
        """Data IO percentage"""
        return metrics_client.physical_data_read_percent(**kwargs)

    @clicktools.metric_command(group)
    def logio(metrics_client, **kwargs):
        """Log IO percentage"""
        return metrics_client.log_write_percent(**kwargs)

    @clicktools.metric_command(group)
    def bytes(metrics_client, **kwargs):
        """Total database size in bytes"""
        return metrics_client.storage(**kwargs)

    @clicktools.metric_command(group)
    def storage(metrics_client, **kwargs):
        """Total database size in bytes"""
        return metrics_client.storage_percent(**kwargs)

    @clicktools.metric_command(group)
    def deadlocks(metrics_client, **kwargs):
        """Deadlocks"""
        return metrics_client.deadlock(**kwargs)
