from django.conf import settings
from django.http import HttpResponseRedirect

DEFAULT_PATH = getattr(settings, "DEFAULT_REDIRECT_URL", "http://www.tirr.com")

def wildcard_redirect(request, path=None):
    if path is not None:
        new_url = DEFAULT_REDIRECT_URL + "/" + path
    return HttpResponseRedirect(new_url)