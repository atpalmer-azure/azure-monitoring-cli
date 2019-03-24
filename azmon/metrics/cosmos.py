

class CosmosMetrics(object):
    def __init__(self, metrics):
        self._metrics = metrics

    def total_requests(self, **kwargs):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        """
        return self._metrics.list_metrics('TotalRequests', 'Count', **kwargs)

    def metadata_requests(self, **kwargs):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        Used to monitor throttles due to metadata requests.
        """
        return self._metrics.list_metrics('MetadataRequests', 'Count', **kwargs)

    def total_request_units(self, **kwargs):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        Used to monitor Total RU usage at a minute granularity. To get average RU consumed per second, use Total aggregation at minute and divide by 60.
        """
        return self._metrics.list_metrics('TotalRequestUnits', 'Total', **kwargs)

    def ru_per_s(self, **kwargs):
        """
        Custom metric derived from total_request_units
        """
        data = self.total_request_units(**kwargs)
        return [ { **item, 'RUs': item['total'] / 60 } for item in data ]

    def provisioned_throughput(self, **kwargs):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        """
        return self._metrics.list_metrics('ProvisionedThroughput', 'Maximum', **kwargs)

    def data_usage(self, **kwargs):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        Used to monitor total data usage at collection and region, minimum granularity should be 5 minutes.

        """
        return self._metrics.list_metrics('DataUsage', 'Total', **kwargs)

    def index_usage(self, **kwargs):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported

        """
        return self._metrics.list_metrics('IndexUsage', 'Total', **kwargs)

    def document_count(self, **kwargs):
        """
        From: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
        Used to monitor document count at collection and region, minimum granularity should be 5 minutes.

        """
        return self._metrics.list_metrics('DocumentCount', 'Total', **kwargs)
