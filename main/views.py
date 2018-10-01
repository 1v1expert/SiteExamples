from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404
from django.template import loader

def get_main_page(request):
    template = loader.get_template('main.html')
    context = {}
    response = HttpResponse(template.render(context, request))
    return response