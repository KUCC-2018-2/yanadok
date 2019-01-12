from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from . import dao


def index(request):
    posts = dao.selectTest()
    template = loader.get_template('yanadock/index.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))