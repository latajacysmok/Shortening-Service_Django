from django_hosts import patterns, host
from django.conf import settings

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', 'kirr.hostsconf.urls', name='wildcard'),
    #host(r'(foo|bar)', 'path.to.urls', name='foo-or-bar'),
)