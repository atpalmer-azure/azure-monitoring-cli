

class CosmosMetrics(object):
    def __init__(self, metrics):
        self._metrics = metrics

    def total_request_units(self):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        Used to monitor Total RU usage at a minute granularity. To get average RU consumed per second, use Total aggregation at minute and divide by 60.
        """
        return self._metrics.list_metrics('TotalRequestUnits', 'Total')

    def ru_per_s(self):
        """
        Custom metric derived from total_request_units
        """
        data = self.total_request_units()
        return [ { **item, 'RUs': item['total'] / 60 } for item in data ]

    def provisioned_throughput(self):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        """
        return self._metrics.list_metrics('ProvisionedThroughput', 'Maximum')

    def data_usage(self):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        Used to monitor total data usage at collection and region, minimum granularity should be 5 minutes.

        """
        return self._metrics.list_metrics('DataUsage', 'Total')

    def index_usage(self):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported

        """
        return self._metrics.list_metrics('IndexUsage', 'Total')

    def document_count(self):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        Used to monitor document count at collection and region, minimum granularity should be 5 minutes.

        """
        return self._metrics.list_metrics('DocumentCount', 'Total')
