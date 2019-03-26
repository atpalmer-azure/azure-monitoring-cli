from ..tools import clicktools


def commands(group):
    @clicktools.metric_command(group)
    def cpu(metrics_client, **kwargs):
        """CPU percentage"""
        return metrics_client.cpu_percent(**kwargs)
