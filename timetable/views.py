# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.views import generic

from . import dao


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

splist = []
def save_sp(request, splist):

    userId = request.user.id
    splist = dao.select_user_timetable(userId)

    kw = None
    st = None
    id = None
    rid = None

    if request.method == "POST":
        st = request.POST.get('st')
        kw = request.POST.get('kw')
        id = request.POST.get('id')
        rid = request.POST.get('rid')

    if kw != None and st != None:
        kw = '"' + kw + '"'
        posts = dao.select_search_results_with_st(st, kw)
    elif kw != None and st == None:
        kw = '"' + kw + '"'
        posts = dao.select_search_results(kw)
    else:
        posts = dao.select_all_courses()

    if id != None and posts[int(id)] not in splist:
        user_courses = dao.select_user_timetable(userId)

        uc_daylist = get_daylist(user_courses)
        uc_starttimelist = get_starttimelist(user_courses)
        uc_endtimelist = get_endtimelist(user_courses)

        sp_daylist = []
        sp_starttimelist = []
        sp_endtimelist = []

        templist = posts[int(id)].get('date_classroom').split('/ ')

        for d in templist:
            sp_daylist.append(d[0])
            sp_starttimelist.append(d[2])
            if d[3] == '-':
                sp_endtimelist.append(d[4])
            else:
                sp_endtimelist.append(d[2])

        is_valid = 1
        for i in range(0, len(sp_daylist)):
            for j in range(0, len(uc_daylist)):
                if sp_daylist[i] == uc_daylist[j]:
                    if int(sp_starttimelist[i]) >= int(uc_starttimelist[j]) and int(sp_starttimelist[i]) <= int(uc_endtimelist[j]):
                        is_valid = 0
                        break
                    elif int(sp_starttimelist[i]) <= int(uc_starttimelist[j]) and int(sp_endtimelist[i]) >= int(uc_starttimelist[j]):
                        is_valid = 0
                        break

        if (is_valid == 1):
            splist.append(posts[int(id)])

    if rid != None:
        del splist[int(rid)]

    return splist


# 메인_시간표 메뉴
class TimetableView(generic.View):
    def get(self, request):
        template = loader.get_template('timetable/timetable.html')

        userId = request.user.id

        if userId != None:
            posts = dao.select_user_timetable(userId)

            idlist = []
            namelist = []
            proflist = []
            dclist = []
            for p in posts:
                for d in p.get('date_classroom').split('/ '):
                    idlist.append(p.get('course_id'))
                    namelist.append(p.get('course_name'))
                    proflist.append(p.get('professor'))
                    dclist.append(d.split(')')[1])

            daylist = get_daylist(posts)
            starttimelist = get_starttimelist(posts)
            endtimelist = get_endtimelist(posts)

            sposlist = [160, 238, 315, 365, 416, 492, 570, 619]
            eposlist = [222.5, 300.5, 356.6, 406.6, 478.5, 554.5, 611.6, 660.6]
            small_area = 63.75

            arealist = get_area(starttimelist, endtimelist, sposlist, eposlist, small_area)
            poslist = get_pos(starttimelist, sposlist)

            context = {
                'posts': posts,
                'idlist': idlist,
                'namelist': namelist,
                'proflist': proflist,
                'dclist': dclist,
                'daylist': daylist,
                'arealist': arealist,
                'poslist': poslist,
                'range': range(0, len(namelist)),
            }
        else:
            context = {}

        return HttpResponse(template.render(context, request))

    # def post(self, request):
    #
    #     if request.method == "POST":
    #         course_id = request.POST.get('id')
    #
    #     return HttpResponseRedirect(reverse('board:board', args=(course_id,)))


#시간표 수정
class UpdateTimetableView(generic.View):

    def get(self, request):
        userId = request.user.id
        posts = dao.select_all_courses()
        selected_posts = dao.select_user_timetable(userId)
        template = loader.get_template('timetable/update_timetable.html')

        daylist = get_daylist(selected_posts)
        starttimelist = get_starttimelist(selected_posts)
        endtimelist = get_endtimelist(selected_posts)

        sposlist = [126, 146, 166, 186, 206, 226, 246, 266]
        eposlist = [145, 165, 185, 205, 225, 245, 265, 285]
        small_area = 19

        arealist = get_area(starttimelist, endtimelist, sposlist, eposlist, small_area)
        poslist = get_pos(starttimelist, sposlist)

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
        userId = request.user.id
        splist = dao.select_user_timetable(userId)
        template = loader.get_template('timetable/update_timetable.html')

        kw = None
        st = None
        id = None
        rid = None
        error_message = None

        if request.method == "POST":
            st = request.POST.get('st')
            kw = request.POST.get('kw')
            id = request.POST.get('id')
            rid = request.POST.get('rid')
            save = request.POST.get('save')

        if kw != None and st != None:
            posts = dao.select_search_results_with_st(st, kw)
        elif kw != None and st == None:
            posts = dao.select_search_results(kw)
        else:
            posts = dao.select_all_courses()

        user_courses = dao.select_user_timetable(userId)

        uc_daylist = get_daylist(user_courses)
        uc_starttimelist = get_starttimelist(user_courses)
        uc_endtimelist = get_endtimelist(user_courses)

        sp_daylist = []
        sp_starttimelist = []
        sp_endtimelist = []

        if id != None:
            templist = posts[int(id)].get('date_classroom').split('/ ')

            for d in templist:
                sp_daylist.append(d[0])
                sp_starttimelist.append(d[2])
                if d[3] == '-':
                    sp_endtimelist.append(d[4])
                else:
                    sp_endtimelist.append(d[2])

            is_valid = 1
            for i in range(0, len(sp_daylist)):
                for j in range(0, len(uc_daylist)):
                    if sp_daylist[i] == uc_daylist[j]:
                        if int(sp_starttimelist[i]) >= int(uc_starttimelist[j]) and int(sp_starttimelist[i]) <= int(uc_endtimelist[j]):
                            is_valid = 0
                            break
                        elif int(sp_starttimelist[i]) <= int(uc_starttimelist[j]) and int(sp_endtimelist[i]) >= int(uc_starttimelist[j]):
                            is_valid = 0
                            break

            if (is_valid == 1):
                error_message = None
            else:
                error_message = '해당 과목과 겹치는 수업이 있습니다.'

        selected_posts = save_sp(request, splist)

        if selected_posts != None:
            daylist = get_daylist(selected_posts)
            starttimelist = get_starttimelist(selected_posts)
            endtimelist = get_endtimelist(selected_posts)

            sposlist = [126, 146, 166, 186, 206, 226, 246, 266]
            eposlist = [145, 165, 185, 205, 225, 245, 265, 285]
            smallarea = 19

            arealist = get_area(starttimelist, endtimelist, sposlist, eposlist, smallarea)
            poslist = get_pos(starttimelist, sposlist)

        splist = save_sp(request, splist)

        dao.update_timetable(splist, userId)

        print(error_message)

        context = {
            'posts': posts,
            'selected_posts': selected_posts,
            'daylist': daylist,
            'arealist': arealist,
            'poslist': poslist,
            'range': range(0, len(daylist)),
            'error_message': error_message,
        }

        return HttpResponse(template.render(context, request))


