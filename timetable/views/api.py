from timetable import dao, services
from yanadok.common.views import ApiView


class TimetableApiView(ApiView):
    def post(self, request):
        services.add_course_to_timetable(request.user, request.POST['course_id'])
        return self.response(dao.select_user_timetable(request.user.id))

    def get(self, request):
        return self.response(dao.select_user_timetable(request.user.id))
