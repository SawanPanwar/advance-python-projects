from django.http import HttpResponse


class SimpleMiddleware(object):
    count = 0

    def __init__(self, get_resp):
        self.get_response = get_resp

    def __call__(self, request):
        SimpleMiddleware.count += 1
        print("Middleware = ", SimpleMiddleware.count)
        # res = self.get_response(request)
        return HttpResponse("<center><h1>Welcome to Middleware</h1></center>")
        # return res
