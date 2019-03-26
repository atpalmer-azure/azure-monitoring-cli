

class SqlMetrics(object):
    def __init__(self, metrics):
        self._metrics = metrics

    def cpu_percent(self, **kwargs):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        """
        return self._metrics.list_metrics('cpu_percent', 'Average', **kwargs)

    def log_write_percent(self, **kwargs):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        """
        return self._metrics.list_metrics('log_write_percent', 'Average', **kwargs)
