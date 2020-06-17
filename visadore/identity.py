from collections import namedtuple

Identity = namedtuple("Identity", "company, model, serial, config")


def _identity_parser(idn_str):
    idn = tuple(idn_str.split(","))
    return Identity(*idn)


def _ident(resource_name, resource_manager, timeout):

    # If not provided, create a pyvisa ResourceManager object
    if not resource_manager:
        import pyvisa

        resource_manager = pyvisa.ResourceManager()

    # open a connection and fetch the instrument IDN string
    with resource_manager.open_resource(resource_name) as inst:
        inst.timeout = timeout
        inst.clear()
        idn = inst.query("*IDN?").strip()
    return _identity_parser(idn)


def compile_namespace(identity):
    return ".".join(["visadore", identity.company, identity.model]).lower()
