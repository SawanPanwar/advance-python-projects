from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.db import connection

from .service.UserService import UserService


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
    list = [{"id": 1, "firstName": "abc", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
            {"id": 2, "firstName": "xyz", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"},
            {"id": 3, "firstName": "pqr", "lastName": "aaa", "email": "abc@gmail.com", "password": "12345"}]
    return render(request, "List.html", {"list": list})


def search(request):
    sql = "select * from sos_user"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    columnName = ("id", "firstName", "lastName", "email", "password")
    res = []
    for x in result:
        print({columnName[i]: x[i] for i, _ in enumerate(x)})
        res.append({columnName[i]: x[i] for i, _ in enumerate(x)})
    print(res)
    return render(request, "List.html", {"list": res})


def test(request):
    if request.method == "POST":
        f = request.POST.get('firstName')
        l = request.POST.get('lastName')
        e = request.POST.get('email')
        p = request.POST.get('password')
        user = UserService()
        user.add(f, l, e, p)
    return render(request, "Registration.html")

def create_session(request):
    request.session['name'] = 'Admin'
    response = "<h1>Welcome To Sessions</h1><br>"
    response += "ID : {0} <br>".format(request.session.session_key)
    return HttpResponse(response)


def access_session(request):
    response = "Name : {0} <br>".format(request.session.get('name'))
    return HttpResponse(response)


def destroy_session(request):
    Session.objects.all().delete()
    return HttpResponse("Session is Destroy")


def setCookies(request):
    if request.method=="POST":
        value = request.POST.get('cookieName')
        res = HttpResponse("<h1>Rays Technologies</h1>")
        res.set_cookie("name", value, max_age=20)
        return res
    return render(request, "SetCookies.html")


def getCookies(request):
    name = request.COOKIES.get('name')
    html = "<h3><center> name = {} </center></h3>".format(name)
    return HttpResponse(html)

def testRedirect(request):
    return redirect('/ORS/Reg')

def index(request):
    return redirect('/ORS/Reg')
