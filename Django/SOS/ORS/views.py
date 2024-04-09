from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm
from .models import User


def hello(request):
    return HttpResponse('<h3>Hello Python</h3>')


def user(request, id=0, name=""):
    message = "User id = " + str(id) + name
    return HttpResponse(message)


def registration(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Registration Successfully.....")
        else:
            return HttpResponse("PLz... fill all fields")

    return render(request, "Registration.html")


def welcome(request):
    return render(request, "Welcome.html", {"firstName": "Indore"})


def list(request):
    list = [{"id": 1, "firstName": "abc", "lastName": "aaa", "loginId": "abc@gmail.com", "password": "12345"},
            {"id": 2, "firstName": "xyz", "lastName": "aaa", "loginId": "abc@gmail.com", "password": "12345"},
            {"id": 3, "firstName": "pqr", "lastName": "aaa", "loginId": "abc@gmail.com", "password": "12345"}]
    return render(request, "List.html", {"list": list})
