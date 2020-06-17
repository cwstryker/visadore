from stevedore import extension

class DynClass:
    
    """Dynamic class docstring"""
    
    def __init__(self):
        """__init__ docstring"""
        pass

    @property
    def features(self):
        """A list of supported instrument features"""
        return self._features


def obj_factory(namespace):
    
    cls_name = "".join([t.capitalize() for t in namespace.split('.')[1:]])
    cls = type(cls_name, (DynClass,), dict(DynClass.__dict__))
    
    mgr = extension.ExtensionManager(
        namespace=namespace,
        invoke_on_load=True,
        invoke_args=(),
    )

    def format_data(ext):
        return (ext.name, ext.obj.get_feature())

    results = mgr.map(format_data)

    features = []
    for name, result in results:
        setattr(cls, name, result)
        features.append(name)
    setattr(cls, "_features", features)

    return cls()

if __name__ == '__main__':

    a = obj_factory('visadore.example1')
    help(a)
    print(a.features)

    b = obj_factory('visadore.example2')
    help(b)
    print(b.complex(2))
    
    c = obj_factory('visadore.example1')
    help(a)
    print(a.simple(3))
