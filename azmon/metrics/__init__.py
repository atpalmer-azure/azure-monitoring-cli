from datetime import datetime, timedelta
from ..tools import datatools


INTERVAL_TIMEDELTAS = {
    'PT1M': timedelta(minutes=1),
    'PT5M': timedelta(minutes=5),
    'PT1H': timedelta(hours=1),
}


class Metrics(object):
    """
    See: https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-supported
    """
    def __init__(self, client, resource_id):
        self._client = client
        self._resource_id = resource_id

    @classmethod
    def create_interface(cls, client, resource_id, interface):
        metrics = cls(client, resource_id)
        return interface(metrics)

    def list_definitions(self):
        for item in self._client.metric_definitions.list(self._resource_id):
            print(item.name)

    def list_metrics(self, metric_names, aggregation, *, interval='PT5M', count=1):
        """
        valid aggregations: Average, Total, Maximum, Minimum, Count
        """
        end_time = datetime.now()
        start_time = end_time - (INTERVAL_TIMEDELTAS[interval] * count)

        data = self._client.metrics.list(
            resource_uri=self._resource_id,
            timespan=f'{start_time}/{end_time}',
            interval=interval,
            metricnames=metric_names,
            aggregation=aggregation,
        )

        result = [
            datatools.dict_clean({
                'name': item.name.localized_value,
                'unit': item.unit.name,
                'timestamp': ts_data_item.time_stamp,
                'total': ts_data_item.total,
                'average': ts_data_item.average,
                'count': ts_data_item.count,
                'maximum': ts_data_item.maximum,
                'minimum': ts_data_item.minimum,
            })
            for item in data.value
            for ts_item in item.timeseries
            for ts_data_item in ts_item.data
        ]

        return result


from .cosmos import CosmosMetrics
from .iothub import IotHubMetrics


__all__ = [
    Metrics,
    CosmosMetrics,
    IotHubMetrics,
]
