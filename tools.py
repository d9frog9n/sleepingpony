import importlib
import sys

from exceptions import WrongPinger
from pingers import Pinger


def load(pinger_dotted_path):
    pinger = None

    parts = pinger_dotted_path.split('.')
    path_c, pinger_name_c = parts[:-1], parts[-1:]

    #checking module.name (two parts min)
    try:
        if path_c and pinger_name_c:
            del path_c, pinger_name_c
            path, pinger_name = '.'.join(parts[:-1]), parts[-1:][0]
        else:
            raise ImportError
        #importing module
        module = importlib.import_module(path)
    except ImportError:
        raise WrongPinger('Wrong module dotted path: %s' % pinger_dotted_path)

    #importing pinger
    try:
        pinger_cls = getattr(module, pinger_name)
    except AttributeError:
        raise WrongPinger('Missed definition of %(name)s at %(path)s' % \
            dict(name=pinger_name, path=path))

    #checking subclassing
    try:
        if pinger_cls and issubclass(pinger_cls, Pinger):
            pinger = pinger_cls
        else:
            raise TypeError
    except TypeError:
        raise WrongPinger('Pinger %(mod)s is not subclass of %(cls)s' % \
            dict(cls=str(Pinger), mod=pinger_dotted_path))

    return pinger_cls


if __name__ == '__main__':
    if len(sys.argv) == 2:
        pinger = load(sys.argv[1])
        if pinger:
            pong = unicode(pinger().ping())
            sys.stdout.write(pong)
            sys.stdout.write('\n')
    else:
        raise SystemExit('Missed path.to.pinger')
