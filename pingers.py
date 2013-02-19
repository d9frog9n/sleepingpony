import httplib


class Pong(object):
    def __init__(self, pong_string=''):
        self.pong_string = unicode(pong_string)

    def __unicode__(self):
        return self.pong_string


class Pinger(object):
    def ping(self):
        raise NotImplemented


class HttpPinger(Pinger):
    proto = 'http'
    host = 'localhost'
    port = httplib.HTTP_PORT
    path = '/'
    method = 'GET'
    timeout = 5

    def ping(self):
        status = 0
        try:
            conn = httplib.HTTPConnection(self.host, port=self.port,
                timeout=self.timeout)
            url = '%(proto)s://%(host)s:%(port)s/%(path)s' % dict(proto=self.proto,
                host=self.host, port=self.port, path=self.path)
            conn.request(self.method, url)
            response = conn.getresponse()
            status = self.is_response_ok(response) and 1 or 0
        except socket.timeout as e:
            pass
        return Pong(status)

    def is_response_ok(self, response):
        return response.status == httplib.OK


class DjangoDBConnectionPinger(Pinger):
    database_settings = {}

    def ping(self):
        status = 0
        from django.conf import settings, global_settings
        my_settings = global_settings
        my_settings.DATABASES = {'default': self.database_settings}
        settings.configure(default_settings=my_settings)
        from django.db import utils as db_utils

        conn_handler = db_utils.ConnectionHandler(my_settings.DATABASES)
        try:
            conn = conn_handler['default']
            try:
                conn.cursor()
            except: #  can't handle `backend`.OperationError
                raise AttributeError
            status = int(conn._valid_connection())
        except AttributeError as e:
            pass
        return Pong(status)


def __get_base_pinger_classes(scope):
    base_classes = []
    for var in scope:
        obj = scope[var]
        try:
            if issubclass(obj, Pinger):
                base_classes.append(obj)
        except TypeError:
            pass
    return base_classes


BASE_PINGERS_CLASSES = __get_base_pinger_classes(locals())
