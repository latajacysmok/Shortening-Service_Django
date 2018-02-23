from django.shortcuts import render
from django.http import HttpResponse
from  django.views import View

def kirr_redirect_views(request, *args, **kwargs):
    return HttpResponse("hello")

class KirrCBView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("hello again")

