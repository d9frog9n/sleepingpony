import importlib


from pingers import Pinger, BASE_PINGERS_CLASSES
from settings import get_settings_pingers_modules


def get_enabled_pingers():
    pingers_classes = []

    for mod in get_settings_pingers_modules():
        try:
            module = importlib.import_module(mod)
        except ImportError:
            continue

        for var in dir(module):
            obj = getattr(module, var)
            try:
                if issubclass(obj, Pinger) and \
                    obj not in BASE_PINGERS_CLASSES:
                    pingers_classes.append(obj)
            except TypeError:
                pass
    return pingers_classes
