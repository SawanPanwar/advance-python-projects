from django.shortcuts import render, redirect
from .service.UserService import UserService
from .utility.DataValidator import DataValidator


def validate(request):
    input_errors = {}
    input_errors['error'] = False
    if (DataValidator.isNull(request.POST["firstName"])):
        input_errors['firstName'] = 'first name is required'
        input_errors['error'] = True
    if (DataValidator.isNull(request.POST["lastName"])):
        input_errors['lastName'] = 'last name is required'
        input_errors['error'] = True
    if (DataValidator.isNull(request.POST["email"])):
        input_errors['email'] = 'email is required'
        input_errors['error'] = True
    if (DataValidator.isNull(request.POST["password"])):
        input_errors['password'] = 'password is required'
        input_errors['error'] = True
    # elif (DataValidator.isPassword(request.POST["password"])):
    #     input_errors['password'] = 'password must contains Password123!'
    #     input_errors['error'] = True
    return input_errors


def user_register(request):
    request_form = {}
    message = ''
    input_errors = {}
    if request.method == "POST":
        request_form['firstName'] = request.POST["firstName"]
        request_form['lastName'] = request.POST["lastName"]
        request_form['email'] = request.POST["email"]
        request_form['password'] = request.POST["password"]
        input_errors = validate(request)
        if not input_errors['error']:
            user = UserService()
            recordExist = user.findByEmail(request_form['email'])
            if len(recordExist) != 0:
                message = 'email already exist'
            else:
                user.add(request_form)
                message = 'User Register Successfully..!!'
    return render(request, "Registration.html", {"message": message, "inputerror": input_errors})


def user_signin(request):
    if request.method == "POST":
        e = request.POST["email"]
        p = request.POST["password"]
        print('data -> ', e, ' ', p)
        user = UserService.auth(e, p)
        if len(user) != 0:
            request.session["firstName"] = user[0].get('firstName')
            return redirect("/ORS/welcome")
        else:
            return redirect("/ORS/signup")
    return render(request, "Login.html")


def add_user(request):
    request_form = {}
    if request.method == "POST":
        request_form['firstName'] = request.POST["firstName"]
        request_form['lastName'] = request.POST["lastName"]
        request_form['email'] = request.POST["email"]
        request_form['password'] = request.POST["password"]
        request_form['id'] = request.POST["id"]
        user = UserService()
        if request.POST["id"] != "":
            user.update(request_form)
        else:
            user.add(request_form)
    return render(request, "User.html")


def user_list(request):
    params = {}
    params['pageNo'] = 1
    params['pageSize'] = 5

    if request.method == "POST":

        if request.POST['operation'] == "search":
            params['firstName'] = request.POST['firstName']

        if request.POST['operation'] == "add":
            return redirect('/ORS/add')

        if request.POST['operation'] == "delete":
            id = request.POST["id"]
            UserService.delete(id)

        if request.POST['operation'] == "next":
            params['pageNo'] = int(request.POST['pageNo'])
            params['pageNo'] += 1

        if request.POST['operation'] == "previous":
            params['pageNo'] = int(request.POST['pageNo'])
            params['pageNo'] -= 1

    user = UserService()
    userList = user.search(params);

    return render(request, "UserList.html", {'userList': userList, 'pageNo': params['pageNo']})


def edit(request, id):
    user = UserService()
    data = user.get(id)
    return render(request, "User.html", {"form": data[0]})


def delete(request, id):
    user = UserService()
    user.delete(id)
    return redirect('/ORS/list')


def welcome(request):
    return render(request, "Welcome.html")


def logout(request):
    request.session['firstName'] = None
    return redirect('/ORS/signin')


def test(request):
    if request.method == "POST":
        print('file => ', request.POST['inputFile'])
    return render(request, "Test.html")
