from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Post
from django.apps import apps
from .forms import PostForm


from . import dao

course = apps.get_model('timetable', 'Course')

class BoardView(generic.View):

    def get(self, request, course_id):
        template = loader.get_template('board/board.html')
        user_id = request.user.id

        posts = dao.select_all_posts(course_id)

        courselist = dao.get_courselist(user_id)
        # print(user_id)
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


def boardRedirection(request):
    return HttpResponseRedirect(reverse('timetable:home'))


class NewPost(generic.View):

    def get(self, request, course_id):
        template = 'board/new_post.html'
        form = PostForm()
        return render(request, template, {'form': form, })

    def post(self, request, course_id):
        template = 'board/new_post.html'
        form = PostForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.course_id = course.objects.get(course_id=course_id)
            post.save()
            return redirect('board:board', course_id)
        else:
            form = PostForm()
        return render(request, template, {'form': form, })


class EditPost(generic.View):

    def get(self, request, post_id):
        template = 'board/new_post.html'
        posting = Post.objects.get(post_id=post_id)
        if posting.user_id != request.user:
            return HttpResponse('잘못된 접근입니다.')
        form = PostForm(instance=posting)
        return render(request, template, {'form': form, })

    def post(self, request, post_id):
        template = 'board/new_post.html'
        posting = Post.objects.get(post_id=post_id)
        course_id = posting.course_id.course_id
        form = PostForm(request.POST, instance=posting)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user
            post.course_id = course.objects.get(course_id=course_id)
            post.save()
            return redirect('board:post', post_id)
        else:
            form = PostForm(instance=posting)
        return render(request, template, {'form': form, })


class PostView(generic.View):
    def get(self, request, post_id):
        template = loader.get_template('board/post.html')

        post = dao.select_post(post_id)
        like_num = dao.get_like_num(post_id)
        course_id = post.get('course_id').course_id
        # print(course_id)

        user_id = request.user.id
        like_active = dao.like_active(post_id, user_id)
        if like_active == True:
            message = '좋아요 취소'
            like_class = 'like_active'
        else:
            message ='좋아요'
            like_class = 'like'

        context = {
            'post': post,
            'like_num': like_num,
            'message': message,
            'like_class': like_class,
            'course_id': course_id,
        }

        return HttpResponse(template.render(context, request))


    def post(self, request, post_id):
        template = loader.get_template('board/post.html')

        if request.method == "POST":
            like = request.POST.get('like')

        user_id = request.user.id
        if like == 'like_active':
            dao.delete_like(post_id, user_id)
            message = '좋아요'
            like_class = 'like'
        else:
            dao.insert_like(post_id, user_id)
            message = '좋아요 취소'
            like_class = 'like_active'

        post = dao.select_post(post_id)
        course_id = post.get('course_id').course_id
        like_num = dao.get_like_num(post_id)

        context = {
            'post': post,
            'like_num': like_num,
            'message': message,
            'like_class': like_class,
            'course_id': course_id,
        }

        return HttpResponse(template.render(context, request))

