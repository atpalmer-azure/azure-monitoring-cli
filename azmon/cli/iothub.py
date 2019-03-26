from ..tools import clicktools


def commands(group):
    @clicktools.metric_command(group)
    def inall(metrics_client, **kwargs):
        """IoT Hub telemetry message send attempts"""
        return metrics_client.ingress_all(**kwargs)

    @clicktools.metric_command(group)
    @clicktools.rename('in')
    def in_(metrics_client, **kwargs):
        """IoT Hub telemetry messages sent"""
        return metrics_client.ingress_success(**kwargs)
