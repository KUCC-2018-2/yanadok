from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .forms import PostForm


class boardView(generic.View):

    def get(self, request):
        template = loader.get_template('board/board.html')

        context = {
        }

        return HttpResponse(template.render(context, request))

def new_post(request):
    template='board/new_post.html'
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()

    else:
        form = PostForm()


    context = {
        'form': form,
    }
    return render(request, template, context)
