

class IotHubMetrics(object):
    def __init__(self, metrics):
        self._metrics = metrics

    def ingress_all(self, **kwargs):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        """
        return self._metrics.list_metrics('d2c.telemetry.ingress.allProtocol', 'Total', **kwargs)

    def ingress_success(self, **kwargs):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        """
        return self._metrics.list_metrics('d2c.telemetry.ingress.success', 'Total', **kwargs)

    def egress_success(self, **kwargs):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        """
        return self._metrics.list_metrics('c2d.commands.egress.complete.success', 'Total', **kwargs)

    def egress_abandoned(self, **kwargs):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        """
        return self._metrics.list_metrics('c2d.commands.egress.abandon.success', 'Total', **kwargs)

    def egress_rejected(self, **kwargs):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        """
        return self._metrics.list_metrics('c2d.commands.egress.reject.success', 'Total', **kwargs)
