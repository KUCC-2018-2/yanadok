from board import dao
from course.models import Course
from yanadok.common.views import ApiView


class TimetableApiView(ApiView):
    def post(self, request):
        course = Course.objects.get(pk=request.POST['course_id'])
        dao.update_timetable([course], request.user)
        return self.response(dao.select_user_timetable(request.user.id))

    def get(self, request):
        return self.response(dao.select_user_timetable(request.user.id))
