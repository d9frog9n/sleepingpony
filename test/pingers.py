from sleepingpony.pingers import Pinger, Pong

class SimplePinger(Pinger):
    def ping(self):
        return Pong(1)

class NotAPinger(object):
    pass