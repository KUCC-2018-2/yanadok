from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import generic


class boardView(generic.View):

    def get(self, request):
        template = loader.get_template('board/board.html')


        context = {

        }

        return HttpResponse(template.render(context, request))