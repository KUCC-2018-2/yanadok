# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

from course.models import CourseTime
from timetable import dao
from timetable.services import get_user_timetable


def get_daylist(posts):
    daylist = []

    for p in posts:
        for d in p.get('date_classroom').split('/ '):
            daylist.append(d[0])

    return daylist


def get_starttimelist(posts):
    starttimelist = []

    for p in posts:
        for d in p.get('date_classroom').split('/ '):
            starttimelist.append(d[2])

    return starttimelist


def get_endtimelist(posts):
    endtimelist = []

    for p in posts:
        for d in p.get('date_classroom').split('/ '):
            if d[3] == '-':
                endtimelist.append(d[4])
            else:
                endtimelist.append(d[2])

    return endtimelist


def get_area(starttimelist, endtimelist, sposlist, eposlist, small_area):
    arealist = []

    for n in range(0, len(starttimelist)):
        if starttimelist[n] == '3' and endtimelist[n] == '4':
            a = small_area
        elif starttimelist[n] == '7' and endtimelist[n] == '8':
            a = small_area
        else:
            a = eposlist[int(endtimelist[n]) - 1] - sposlist[int(starttimelist[n]) - 1]

        arealist.append(a)

    return arealist


def get_pos(starttimelist, sposlist):
    poslist = []

    for n in range(0, len(starttimelist)):
        sp = sposlist[int(starttimelist[n]) - 1]
        poslist.append(sp)

    return poslist


# 메인_시간표 메뉴
# class TimetableView(generic.View):
#     def get(self, request):
#         if request.user.is_authenticated:
#             template = loader.get_template('timetable/timetable.html')
#
#             userId = request.user.id
#
#             if userId != None:
#                 posts = dao.select_user_timetable(userId)
#
#                 idlist = []
#                 namelist = []
#                 proflist = []
#                 dclist = []
#                 for p in posts:
#                     for d in p.get('date_classroom').split('/ '):
#                         idlist.append(p.get('course_id'))
#                         namelist.append(p.get('course_name'))
#                         proflist.append(p.get('professor'))
#                         dclist.append(d.split(')')[1])
#
#                 daylist = get_daylist(posts)
#                 starttimelist = get_starttimelist(posts)
#                 endtimelist = get_endtimelist(posts)
#
#                 sposlist = [160, 238, 315, 365, 416, 492, 570, 619]
#                 eposlist = [222.5, 300.5, 356.6, 406.6, 478.5, 554.5, 611.6, 660.6]
#                 small_area = 63.75
#
#                 arealist = get_area(starttimelist, endtimelist, sposlist, eposlist, small_area)
#                 poslist = get_pos(starttimelist, sposlist)
#
#                 context = {
#                     'posts': posts,
#                     'idlist': idlist,
#                     'namelist': namelist,
#                     'proflist': proflist,
#                     'dclist': dclist,
#                     'daylist': daylist,
#                     'arealist': arealist,
#                     'poslist': poslist,
#                     'range': range(0, len(namelist)),
#                 }
#             else:
#                 context = {}
#
#             return HttpResponse(template.render(context, request))
#         else:
#             return HttpResponseRedirect(reverse('user:login'))

class TimetableView(generic.View):
    day_names = [day[0] for day in CourseTime.DAY_CHOICES]

    def get(self, request):
        if request.user.is_authenticated:
            template = loader.get_template('timetable/timetable.html')
            timetable = get_user_timetable(request.user)
            context = {
                'long_period_classes': [1, 2, 5, 6],
                'max_classes': range(1, 9),
                'day_names': TimetableView.day_names,
                'timetable': timetable
            }
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect(reverse('user:login'))

    def __map_course_by_time(self, timetable):
        result = {}
        for course in timetable:
            for course_time in course['course_times']:
                result[self.__get_coord_of_course_time(course_time)] = {
                    'course_name': course['course_name'],
                    'course_id': course['course_id']
                }

    def __get_coord_of_course_time(self, course_time):
        return course_time['order'], TimetableView.day_names.index(course_time['course_day'])


# 시간표 수정
class UpdateTimetableView(generic.View):
    def get(self, request):
        template = loader.get_template('timetable/update_timetable.html')
        return HttpResponse(template.render({}, request))
