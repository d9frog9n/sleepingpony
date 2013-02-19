from django.conf import settings

SLEEPINGPONY_PINGERS_MODULES = ('sleepingpony.default_pingers', )
SLEEPINGPONY_APP_STATUS_PAGE = 'app-status.html'


def get_settings_pingers_modules():
    pingers_modules = SLEEPINGPONY_PINGERS_MODULES
    try:
        pingers_modules = settings.SLEEPINGPONY_PINGERS_MODULES
    except AttributeError:
        pass
    return pingers_modules

def get_app_status_page_name():
    page_name = SLEEPINGPONY_APP_STATUS_PAGE
    try:
        page_name = settings.SLEEPINGPONY_APP_STATUS_PAGE
    except AttributeError:
        pass
    return page_name
