from django.http import HttpResponse

from ..models import RequestData


class SimpleMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        obj = RequestData()
        obj.http_host = request.META.get("HTTP_HOST")
        obj.remote_host = request.META.get("REMOTE_HOST")
        obj.remote_user = request.META.get("REMOTE_USER")
        obj.remote_address = request.META.get("REMOTE_ADDR")
        obj.http_user_agent = request.META.get("HTTP_USER_AGENT")
        obj.save()

        # print(request.META)
        return response
