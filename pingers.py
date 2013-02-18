class Pong(object):
    def __init__(self, pong_string=''):
        self.pong_string = unicode(pong_string)

    def __unicode__(self):
        return self.pong_string


class Pinger(object):
    def ping(self):
        raise NotImplemented