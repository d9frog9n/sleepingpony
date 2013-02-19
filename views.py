from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from exceptions import WrongPinger
from tools import load
from utils import get_enabled_pingers


def app_status_page(request):
    def p2dp(p):
        return '%s.%s' % (p.__module__, p.__name__)

    context = {'pingers': [p2dp(p)
        for p in get_enabled_pingers()]}

    return render_to_response('sleepingpony/app-status.html', context,
        context_instance=RequestContext(request))


def pinger_ping(request, pinger_class):
    resp, status = '', 200
    try:
        pinger = load(pinger_class)
        resp = pinger().ping()
    except WrongPinger:
        status = 406
    return HttpResponse(resp, status=status)
