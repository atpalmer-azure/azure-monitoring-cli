from ..tools import clicktools


def commands(group):
    @clicktools.metric_command(group)
    def cpu(metrics_client, **kwargs):
        """CPU percentage"""
        return metrics_client.cpu_percent(**kwargs)

    @clicktools.metric_command(group)
    def logio(metrics_client, **kwargs):
        """Log IO percentage"""
        return metrics_client.log_write_percent(**kwargs)
