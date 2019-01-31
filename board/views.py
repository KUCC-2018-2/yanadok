from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from timetable.models import Course
from .models import Post, Comment, PostLike
from django.apps import apps
from .forms import PostForm, CommentForm, PostLikeForm

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
        return HttpResponse(template.render({'form': form, }, request))

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
            return HttpResponse(template.render({'form': form, }, request))


class EditPost(generic.View):

    def get(self, request, post_id):
        template = loader.get_template('board/new_post.html')
        posting = Post.objects.get(post_id=post_id)
        if posting.user_id != request.user:
            return HttpResponse('잘못된 접근입니다.')
        form = PostForm(instance=posting)
        return HttpResponse(template.render({'form': form, }, request))

    def post(self, request, post_id):
        template = loader.get_template('board/new_post.html')
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
            return HttpResponse(template.render({'form': form, }, request))


class PostView(generic.View):
    def get(self, request, post_id):
        template = loader.get_template('board/post.html')
        form = CommentForm()
        like_form = PostLikeForm()
        comments = Comment.objects.filter(post_id=post_id)
        post = Post.objects.get(post_id=post_id)
        current_course = Course.objects.get(course_id=post.course_id.course_id)
        post_like = PostLike.objects.filter(post_id=post_id)
        check = PostLike.objects.filter(user_id=request.user.id).exists()

        context = {
            'form': form,
            'like_form': like_form,
            'comments': comments,
            'post': post,
            'course': current_course,
            'post_like': post_like,
            'check': check,
        }
        return HttpResponse(template.render(context, request))

    def post(self, request, post_id):
        template = loader.get_template('board/post.html')
        form = CommentForm(request.POST or None)
        like_form = PostLikeForm(request.POST or None)
        comments = Comment.objects.filter(post_id=post_id)
        post = Post.objects.get(post_id=post_id)
        current_course = Course.objects.get(course_id=post.course_id.course_id)
        post_like = PostLike.objects.filter(post_id=post_id)
        check = PostLike.objects.filter(user_id=request.user.id).exists()

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user_id = request.user
            new_comment.post_id = Post.objects.get(post_id=post_id)
            new_comment.save()
            return redirect('board:post', post_id)

        elif like_form.is_valid():

            if check:
                pass
                old_like = PostLike.objects.get(user_id=request.user.id)
                old_like.delete()
            else:
                new_like = like_form.save(commit=False)
                new_like.user_id = request.user
                new_like.post_id = Post.objects.get(post_id=post_id)
                new_like.save()
            return redirect('board:post', post_id)

        else:
            form = CommentForm()
            context = {
                'form': form,
                'like_form': like_form,
                'comments': comments,
                'post': post,
                'course': current_course,
                'post_like': post_like,
                'check': check,
            }
            return HttpResponse(template.render(context, request))




