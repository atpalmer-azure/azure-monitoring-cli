import toml


class ResourceConfig(object):
    def __init__(self, config):
        self._config = config

    @classmethod
    def load_toml(cls, filename):
        with open(filename) as f:
            config = toml.load(f)
        return cls(config)

    def get_resource(self, environment, resource):
        return self._config[environment][resource]
