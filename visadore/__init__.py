from .instrument import instrument_factory

__VERSION__ = "0.1.0"


def get(resource_name, resource_manager, identity=None, timeout=10):
	return instrument_factory(resource_name, resource_manager, identity, timeout)
