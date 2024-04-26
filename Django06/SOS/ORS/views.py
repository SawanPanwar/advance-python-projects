from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


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
