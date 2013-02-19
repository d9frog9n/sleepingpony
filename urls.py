from django.conf.urls.defaults import patterns, url

from settings import get_app_status_page_name
import views

page_name = get_app_status_page_name()

urlpatterns = patterns('',
    url('^%s$' % page_name, views.app_status_page, name='app_status_page'),
    url('^ping/(?P<pinger_class>\S+)$', views.pinger_ping, name='pinger_ping'),
)