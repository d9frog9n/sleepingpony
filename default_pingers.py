from django.conf import settings

from pingers import DjangoDBConnectionPinger


def create_dbpingers_classes(databases):
    classes = []
    for da, ds in databases.items():
        cls = type('%s_%s' % (da, DjangoDBConnectionPinger.__name__),
            (DjangoDBConnectionPinger, ),
            {'database_settings': ds})
        classes.append(cls)
    return classes


#exporting `db_alias`_DjangoDBConnectionPinger class to locals
for cls in create_dbpingers_classes(settings.DATABASES):
    locals()[cls.__name__] = cls
