import nose as n


from sleepingpony.exceptions import WrongPinger
from sleepingpony.tools import load

@n.tools.raises(WrongPinger)
def load_wrong_path_test():
    load('wrong_dotted_path')

@n.tools.raises(WrongPinger)
def load_missed_pinger_test():
    load('sleepingpony.test.pingers')

@n.tools.raises(WrongPinger)
def load_not_a_pinger_test():
    load('sleepingpony.test.pingers.NotAPinger')

def load_ok_test():
    load('sleepingpony.test.pingers.SimplePinger')
