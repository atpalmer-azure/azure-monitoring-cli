from ..tools import clicktools


def commands(group):
    @clicktools.metric_command(group)
    def inall(metrics_client, **kwargs):
        """Number of device-to-cloud telemetry messages attempted to be sent to your IoT hub"""
        return metrics_client.ingress_all(**kwargs)

    @clicktools.metric_command(group)
    @clicktools.rename('in')
    def in_(metrics_client, **kwargs):
        """Number of device-to-cloud telemetry messages sent successfully to your IoT hub"""
        return metrics_client.ingress_success(**kwargs)
