from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import PostForm

from . import dao


class BoardView(generic.View):

    def get(self, request, course_id):
        template = loader.get_template('board/board.html')
        userId = request.user.id

        posts = dao.select_all_posts(course_id)

        courselist = dao.get_courselist(userId)
        course_name = dao.get_course_name(course_id)
        course_idlist = []
        for course in courselist:
            course_idlist.append(course['course_id'])

        page_len = int(len(posts) / 10) + 1
        page_range = range(1, page_len+1)

        page_num = 1
        current_postlist = []

        for n in range((page_num  - 1) * 10, page_num * 10):
            if n < len(posts):
                current_postlist.append(posts[n])

        userlist = dao.get_userlist(current_postlist)

        context = {
            'course_id': course_id,
            'course_name': course_name,
            'posts': posts,
            'current_postlist': current_postlist,
            'userlist': userlist,
            'courselist': courselist,
            'course_idlist': course_idlist,
            'page_range': page_range,
        }

        return HttpResponse(template.render(context, request))

    def post(self, request, course_id):
        template = loader.get_template('board/board.html')
        userId = request.user.id

        if request.method == "POST":
            course_id = request.POST.get('course_id')
            post_type = request.POST.get('post_type')

        course_name = dao.get_course_name(course_id)

        if post_type == None:
            posts = dao.select_all_posts(course_id)
        elif post_type == '스터디팀플':
            posts = dao.select_study_posts(course_id)
        else:
            posts = dao.select_all_posts(course_id)

        courselist = dao.get_courselist(userId)
        course_idlist = []

        for course in courselist:
            course_idlist.append(course['course_id'])

        page_len = int(len(posts) / 10) + 1
        page_range = range(1, page_len + 1)

        page_num = 1
        current_postlist = []

        for n in range((page_num - 1) * 10, page_num * 10):
            if n < len(posts):
                current_postlist.append(posts[n])

        userlist = dao.get_userlist(current_postlist)

        context = {
            'course_id': course_id,
            'course_name': course_name,
            'posts': posts,
            'current_postlist': current_postlist,
            'userlist': userlist,
            'courselist': courselist,
            'course_idlist': course_idlist,
            'page_range': page_range,
            'post_type': post_type,
        }

        return HttpResponse(template.render(context, request))


class BoardRedirectionView(generic.View):
    def get(self, request):
        return HttpResponseRedirect(reverse('timetable:home'))

    def post(self, request):
        return HttpResponseRedirect(reverse('timetable:home'))


def new_post(request, course_id):
    template = 'board/new_post.html'
    form = PostForm(request.POST or None)
    user_id = request.user.id
    if form.is_valid():
        form.save()

    else:
        form = PostForm()

    context = {
        'form': form,
        'course_id': course_id,
        'user_id': user_id,
    }
    return render(request, template, context)


class NewPost(generic.View):

    def get(self, request, course_id):
        template = 'board/new_post.html'
        form = PostForm(request.POST or None)
        user_id = request.user.id

        context = {
            'form': form,
            'course_id': course_id,
            'user_id': user_id,
        }
        return render(request, template, context)

    def post(self, request, course_id):
        template = 'board/new_post.html'
        form = PostForm(request.POST or None)
        user_id = request.user.id
        if form.is_valid():
            form.save()
            return redirect('board:board', course_id)
        else:
            form = PostForm()

        context = {
            'form': form,
            'course_id': course_id,
            'user_id': user_id,
        }
        return render(request, template, context)

