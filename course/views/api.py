from course import services
from yanadok.common.views import ApiView


class CourseListApiView(ApiView):
    def get(self, request):
        criteria = request.GET.get('criteria')
        search_keyword = request.GET.get('search_keyword')
        return self.response(services.get_courses(request.user, criteria, search_keyword))

