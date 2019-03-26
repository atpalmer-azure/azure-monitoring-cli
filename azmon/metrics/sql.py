

class SqlMetrics(object):
    def __init__(self, metrics):
        self._metrics = metrics

    def cpu_percent(self, **kwargs):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        """
        return self._metrics.list_metrics('cpu_percent', 'Total', **kwargs)
