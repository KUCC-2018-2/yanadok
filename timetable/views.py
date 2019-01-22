from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import generic

from . import dao


def getDayList(posts):
    daylist = []

    for p in posts:
        for d in p.get('date_classroom').split('/ '):
            daylist.append(d[0])

    return daylist


def getStartTimeList(posts):
    starttimelist = []

    for p in posts:
        for d in p.get('date_classroom').split('/ '):
            starttimelist.append(d[2])

    return starttimelist


def getEndTimeList(posts):
    endtimelist = []

    for p in posts:
        for d in p.get('date_classroom').split('/ '):
            if d[3] == '-':
                endtimelist.append(d[4])
            else:
                endtimelist.append(d[2])

    return endtimelist


def getArea(starttimelist, endtimelist, sposlist, eposlist, smallarea):
    arealist = []

    for n in range(0, len(starttimelist)):
        if starttimelist[n] == '3' and endtimelist[n] == '4':
            a = smallarea
        elif starttimelist[n] == '7' and endtimelist[n] == '8':
            a = smallarea
        else:
            a = eposlist[int(endtimelist[n]) - 1] - sposlist[int(starttimelist[n]) - 1]

        arealist.append(a)

    return arealist


def getPos(starttimelist, sposlist):
    poslist = []

    for n in range(0, len(starttimelist)):
        sp = sposlist[int(starttimelist[n]) - 1]
        poslist.append(sp)

    return poslist


splist = dao.selectUserTimetable()
def saveSP(request):
    if request.method == "POST":
        st = request.POST.get('st')
        kw = request.POST.get('kw')
        index = request.POST.get('index')
        rindex = request.POST.get('rindex')

    if kw != None:
        kw = '"' + kw + '"'
        posts = dao.selectSearchResultsWithST(st, kw)

    elif st == None:
        posts = dao.selectSearchResults(kw)
    else:
        posts = dao.selectAllCourses()

    if index != None and posts[int(index)] not in splist:
        splist.append(posts[int(index)])

    if rindex != None:
        del splist[int(rindex)]

    return splist


# 시간표 메뉴
class timetableView(generic.View):
    def get(self, request):
        dao.updateTimetable(splist)
        posts = dao.selectUserTimetable()
        template = loader.get_template('timetable/timetable.html')

        namelist = []
        proflist = []
        dclist = []
        for p in posts:
            for d in p.get('date_classroom').split('/ '):
                namelist.append(p.get('course_name'))
                proflist.append(p.get('professor'))
                dclist.append(d.split(')')[1])

        daylist = getDayList(posts)
        starttimelist = getStartTimeList(posts)
        endtimelist = getEndTimeList(posts)

        sposlist = [160, 238, 315, 365, 416, 492, 570, 619]
        eposlist = [222.5, 300.5, 356.6, 406.6, 478.5, 554.5, 611.6, 660.6]
        smallarea = 41.6

        arealist = getArea(starttimelist, endtimelist, sposlist, eposlist, smallarea)
        poslist = getPos(starttimelist, sposlist)

        context = {
            'posts': posts,
            'namelist': namelist,
            'proflist': proflist,
            'dclist': dclist,
            'daylist': daylist,
            'arealist': arealist,
            'poslist': poslist,
            'range': range(0, len(namelist)),
        }

        return HttpResponse(template.render(context, request))

#시간표 수정
class updateTimetableView(generic.View):

    def get(self, request):
        posts = dao.selectAllCourses()
        selected_posts = dao.selectUserTimetable()
        template = loader.get_template('timetable/update_timetable.html')

        daylist = getDayList(selected_posts)
        starttimelist = getStartTimeList(selected_posts)
        endtimelist = getEndTimeList(selected_posts)

        sposlist = [126, 146, 166, 186, 206, 226, 246, 266]
        eposlist = [145, 165, 185, 205, 225, 245, 265, 285]
        smallarea = 19

        arealist = getArea(starttimelist, endtimelist, sposlist, eposlist, smallarea)
        poslist = getPos(starttimelist, sposlist)

        context = {
            'posts': posts,
            'selected_posts': selected_posts,
            'daylist': daylist,
            'arealist': arealist,
            'poslist': poslist,
            'range': range(0, len(daylist)),
        }

        return HttpResponse(template.render(context, request))

    def post(self, request):
        template = loader.get_template('timetable/update_timetable.html')

        if request.method == "POST":
            st = request.POST.get('st')
            kw = request.POST.get('kw')
            index = request.POST.get('index')
            rindex = request.POST.get('rindex')
            save = request.POST.get('save')

        if kw != None and st != None:
            kw = '"' + kw + '"'
            posts = dao.selectSearchResultsWithST(st, kw)
        elif kw != None and st == None:
            kw = '"' + kw + '"'
            posts = dao.selectSearchResults(kw)
        else:
            posts = dao.selectAllCourses()

        if index != None or rindex != None:
            selected_posts = saveSP(request)
        else:
            selected_posts = splist

        if selected_posts != None:
            daylist = getDayList(selected_posts)
            starttimelist = getStartTimeList(selected_posts)
            endtimelist = getEndTimeList(selected_posts)

            sposlist = [126, 146, 166, 186, 206, 226, 246, 266]
            eposlist = [145, 165, 185, 205, 225, 245, 265, 285]
            smallarea = 19

            arealist = getArea(starttimelist, endtimelist, sposlist, eposlist, smallarea)
            poslist = getPos(starttimelist, sposlist)

        context = {
            'posts': posts,
            'selected_posts': selected_posts,
            'daylist': daylist,
            'arealist': arealist,
            'poslist': poslist,
            'range': range(0, len(daylist)),
        }

        return HttpResponse(template.render(context, request))


