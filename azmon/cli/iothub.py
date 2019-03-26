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

    @clicktools.metric_command(group)
    def commands(metrics_client, **kwargs):
        """Number of cloud-to-device commands completed successfully by the device"""
        return metrics_client.egress_success(**kwargs)

    @clicktools.metric_command(group)
    def abandoned(metrics_client, **kwargs):
        """Number of cloud-to-device commands abandoned by the device"""
        return metrics_client.egress_abandoned(**kwargs)

    @clicktools.metric_command(group)
    def rejected(metrics_client, **kwargs):
        """Number of cloud-to-device commands rejected by the device"""
        return metrics_client.egress_rejected(**kwargs)

    @clicktools.metric_command(group)
    def devices(metrics_client, **kwargs):
        """Number of devices registered to your IoT hub"""
        return metrics_client.total_devices(**kwargs)
