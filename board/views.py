from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Post
from django.apps import apps
from .forms import PostForm

from django.shortcuts import render


from . import dao

course = apps.get_model('timetable', 'Course')
user = apps.get_model('user', 'User')


class BoardView(generic.View):

    def get(self, request, course_id):
        template = loader.get_template('board/board.html')
        user_id = request.user.id

        posts = dao.select_all_posts(course_id)

        courselist = dao.get_courselist(user_id)
        course_name = dao.get_course_name(course_id)
        course_idlist = []
        for course in courselist:
            course_idlist.append(course['course_id'])

        notice_posts = dao.select_notice_posts(course_id)

        context = {
            'course_id': course_id,
            'course_name': course_name,
            'posts': posts,
            'notice_posts': notice_posts,
            'courselist': courselist,
            'course_idlist': course_idlist,
        }

        return HttpResponse(template.render(context, request))

    def post(self, request, course_id):
        template = loader.get_template('board/board.html')
        userId = request.user.id

        if request.method == "POST":
            course_id = request.POST.get('course_id')
            post_type = request.POST.get('post_type')
            key_word = request.POST.get('kw')

        course_name = dao.get_course_name(course_id)

        if post_type == None:
            posts = dao.select_all_posts(course_id)
        elif post_type == '스터디팀플':
            posts = dao.select_study_posts(course_id)
        else:
            posts = dao.select_all_posts(course_id)

        if key_word != None:
            results = []
            for post in posts:
                if key_word in post['title']:
                    results.append(post)
            posts = results

        courselist = dao.get_courselist(userId)
        course_idlist = []

        for course in courselist:
            course_idlist.append(course['course_id'])

        notice_posts = dao.select_notice_posts(course_id)

        context = {
            'course_id': course_id,
            'course_name': course_name,
            'posts': posts,
            'notice_posts': notice_posts,
            'courselist': courselist,
            'course_idlist': course_idlist,
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

        user_id = request.user.id
        like_active = dao.like_active(post_id, user_id)
        if like_active == True:
            message = '좋아요 취소'
            like_class = 'like_active'
        else:
            message ='좋아요'
            like_class = 'like'

        comment_list = dao.select_all_comments(post_id)

        context = {
            'user_id': user.objects.filter(id=user_id)[0],
            'post': post,
            'like_num': like_num,
            'message': message,
            'like_class': like_class,
            'course_id': course_id,
            'comment_list': comment_list,
        }

        return HttpResponse(template.render(context, request))

    def post(self, request, post_id):
        template = loader.get_template('board/post.html')
        message = ''
        like_class = ''

        if request.method == "POST":
            like = request.POST.get('like')
            message = request.POST.get('message')
            comment_content = request.POST.get('comment_content')
            comment_action = request.POST.get('comment_action')
            index = request.POST.get('index')

        user_id = request.user.id
        if like == 'like_active':
            dao.delete_like(post_id, user_id)
            message = '좋아요'
            like_class = 'like'
        elif like == 'like':
            dao.insert_like(post_id, user_id)
            message = '좋아요 취소'
            like_class = 'like_active'

        if comment_action == 'insert':
            dao.insert_comment(post_id, user_id, comment_content)
        elif comment_action == 'delete':
            comment_list = dao.select_all_comments(post_id)
            dao.delete_comment(comment_list[int(index)].get('comment_id'), user_id)

        post = dao.select_post(post_id)
        course_id = post.get('course_id').course_id
        like_num = dao.get_like_num(post_id)
        comment_list = dao.select_all_comments(post_id)

        context = {
            'user_id': user.objects.filter(id=user_id)[0],
            'post': post,
            'like_num': like_num,
            'message': message,
            'like_class': like_class,
            'course_id': course_id,
            'comment_list': comment_list,
        }

        return HttpResponse(template.render(context, request))

