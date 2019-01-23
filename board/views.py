from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .forms import PostForm

from . import dao


class boardView(generic.View):

    def get(self, request, course_id):
        template = loader.get_template('board/board.html')
        userId = request.user.id

        posts = dao.selectAllPosts(course_id)

        courselist = dao.getCourseList(userId)
        course_name = dao.getCourseName(course_id)
        courseIdList = []
        for course in courselist:
            courseIdList.append(course['course_id'])

        pageLen = int(len(posts) / 10) + 1
        pageRange = range(1, pageLen+1)

        pageNum = 1
        currentPostList = []

        for n in range((pageNum - 1) * 10, (pageNum) * 10):
            if n < len(posts):
                currentPostList.append(posts[n])

        userlist = dao.getUserList(currentPostList)

        context = {
            'course_id': course_id,
            'course_name': course_name,
            'posts': posts,
            'currentPostList': currentPostList,
            'userlist': userlist,
            'courselist': courselist,
            'courseIdList': courseIdList,
            'pageRange': pageRange,
        }

        return HttpResponse(template.render(context, request))

    def post(self, request, course_id):
        template = loader.get_template('board/board.html')
        userId = request.user.id

        if request.method == "POST":
            course_id = request.POST.get('course_id')
            post_type = request.POST.get('post_type')

        course_name = dao.getCourseName(course_id)

        if post_type == None:
            posts = dao.selectAllPosts(course_id)
        elif post_type == '스터디팀플':
            posts = dao.selectStudyPosts(course_id)
        else:
            posts = dao.selectAllPosts(course_id)

        courselist = dao.getCourseList(userId)
        courseIdList = []

        for course in courselist:
            courseIdList.append(course['course_id'])

        pageLen = int(len(posts) / 10) + 1
        pageRange = range(1, pageLen + 1)

        pageNum = 1
        currentPostList = []

        for n in range((pageNum - 1) * 10, (pageNum) * 10):
            if n < len(posts):
                currentPostList.append(posts[n])

        userlist = dao.getUserList(currentPostList)

        context = {
            'course_id': course_id,
            'course_name': course_name,
            'posts': posts,
            'currentPostList': currentPostList,
            'userlist': userlist,
            'courselist': courselist,
            'courseIdList': courseIdList,
            'pageRange': pageRange,
            'post_type': post_type,
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
