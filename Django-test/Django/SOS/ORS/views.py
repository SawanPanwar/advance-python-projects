from django.shortcuts import render, redirect
from .service.UserService import UserService


def user_register(request):
    if request.method == "POST":
        f = request.POST["firstName"]
        l = request.POST["lastName"]
        e = request.POST["email"]
        p = request.POST["password"]
        UserService.add(f, l, e, p)
        return redirect('/ORS/signin')
    return render(request, "Regisgtration.html")


def user_signin(request):
    if request.method == "POST":
        e = request.POST["email"]
        p = request.POST["password"]
        print('data -> ', e, ' ', p)
        user = UserService.auth(e, p)
        if user is not None:
            request.session["firstName"] = user[0].get('firstName')
            return redirect("/ORS/welcome")
        else:
            return redirect("/ORS/Reg")
    return render(request, "Login.html")


def add_user(request):
    if request.method == "POST":
        f = request.POST["firstName"]
        l = request.POST["lastName"]
        e = request.POST["email"]
        p = request.POST["password"]
        user = UserService()
        user.add(f, l, e, p)
        return redirect('/ORS/add')
    return render(request, "User.html")


def user_list(request):
    fname = ''
    if request.method == "POST":
        if request.POST['operation'] == "add":
            return redirect('/ORS/add')
        if request.POST['operation'] == "delete":
            id = request.POST["id"]
            UserService.delete(id)
        if request.POST['operation'] == "search":
            fname = request.POST['firstName']
    user = UserService()
    userList = user.search(fname);
    return render(request, "UserList.html", {'userList': userList})


def welcome(request):
    return render(request, "Welcome.html")
