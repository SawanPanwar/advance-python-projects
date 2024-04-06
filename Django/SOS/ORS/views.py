from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse('<h3>Hello Python</h3>')


def user(request, id=0, name=""):
    message = "User id = " + str(id) + name
    return HttpResponse(message)


def registration(request):
    if request.method=="POST":
        return HttpResponse("<h1>Registration Successfully..!!</h1>")
    return render(request,"Registration.html")

def welcome(request):
    return render(request, "Welcome.html")
