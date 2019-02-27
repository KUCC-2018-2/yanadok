import json
from collections import Iterable

from django.core import serializers
from django.http import JsonResponse
from django.views import View


class ApiView(View):
    def response(self, data, status=200, fields=None):
        payload = self.__serialize_data(data, fields)
        return JsonResponse({
            'status': "success" if status < 400 else "fail",
            'data': payload
        }, status=status)

    def __serialize_data(self, data, fields):
        if isinstance(data, dict):
            return data
        if isinstance(data, Iterable):
            return self.__serialize(data, fields)

        return self.__serialize([data], fields)
    
    def __serialize(self, data, fields):
        serialized = json.loads(serializers.serialize('json', data, fields=fields))
        result = []
        for item in serialized:
            item['fields']['id'] = item['pk']
            result.append(item['fields'])
        return result




