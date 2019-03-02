import json
import logging
import traceback

from django.http import JsonResponse
from django.views import View

from yanadok.exceptions import YanadokBaseException


class ApiView(View):
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            request.POST = json.loads(request.body)
        try:
            return super().dispatch(request, *args, **kwargs)
        except YanadokBaseException as e:
            return self.response(data=e.message, status=e.status)
        except Exception as e:
            traceback.print_exc()
            return self.response(data='에러가 발생했습니다. 잠시 뒤에 다시 시도해주세요.', status=500)

    def response(self, data="", status=200):
        return JsonResponse({
            'status': "success" if status < 400 else "fail",
            'data': data
        }, status=status)



