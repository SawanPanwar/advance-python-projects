import logging
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import MarksheetForm
from .models import Marksheet

logger = logging.getLogger(__name__)


def signUp(request):
    if request.method == "POST":
        # get the UserData from Form
        userName = request.POST["userName"]
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        email = request.POST["email"]
        password = request.POST["password"]
        print("FOrm data Received")
        # create user Object
        obj = User.objects.create_superuser(userName, email, password)
        obj.first_name = firstName
        obj.last_name = lastName
        # print("Object Created")
        # save to the DB
        obj.save()
        # print("data saved")
        messages.success(request, "User Crated Successfully")
    return render(request, "Registration.html")


def signIn(request):
    if request.method == "POST":
        # get the UserData from Form
        userName = request.POST["userName"]
        password = request.POST["password"]
        user = authenticate(username=userName, password=password)
        if user is not None:
            request.session["userName"] = userName
            login(request, user)
            return redirect("WELCOME")
        else:
            messages.warning(request, "Invalid User")
    return render(request, "Login.html")


@login_required()
def welcome(request):
    return render(request, "Welcome.html", {"name": request.session.get("userName")})


def destroy(request):
    logout(request)
    messages.success(request, "You are logged out successfully")
    return redirect("SIGN_IN")


@login_required()
def add_marksheet(request):
    form = MarksheetForm()
    if request.method == "POST":
        form = MarksheetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Marksheet Added Successfully")
    return render(request, "Marksheet.html", context={"form": form, "name": request.session.get("userName")})


@login_required()
def getAll_marksheet(request):
    objects = Marksheet.objects.all()
    return render(request, "MarksheetList.html", {"data": objects, "name": request.session.get("userName")})


@login_required()
def edit_marksheet(request, id):
    obj = Marksheet.objects.get(id=id)
    form = MarksheetForm(instance=obj)
    if request.method == "POST":
        form = MarksheetForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Marksheet Updated Successfully")
            return redirect("/ORS/list")
    return render(request, "Marksheet.html", {"form": form, "id": id, "name": request.session.get("userName")})


@login_required()
def delete_marksheet(request, id):
    obj = Marksheet.objects.get(id=id)
    obj.delete()
    messages.success(request, "Marksheet Deleted Successfully")
    return redirect("/ORS/list")


def test_logging(request):
    try:
        c = 10 / 0
    except Exception as e:
        logger.info(e)
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.fatal("fatal message")
    return HttpResponse('<h1>Looger Works..!!!</h1>');
