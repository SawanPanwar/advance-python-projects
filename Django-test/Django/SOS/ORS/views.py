from django.shortcuts import render, redirect

from .service.MarksheetService import MarksheetService
from .service.UserService import UserService
from .utility.DataValidator import DataValidator
from .models import Files
import pandas as pd


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
        excel_file = request.FILES['inputFile']
        df = pd.read_excel(excel_file)

        for index, row in df.iterrows():
            files = Files(
                name=row['name'],
                role=row['role'],
            )
            files.save()

    return render(request, "Test.html")


def add_marksheet(request):
    request_form = {}
    message = ''
    if request.method == "POST":
        request_form['rollNo'] = request.POST["rollNo"]
        request_form['name'] = request.POST["name"]
        request_form['physics'] = request.POST["physics"]
        request_form['chemistry'] = request.POST["chemistry"]
        request_form['maths'] = request.POST["maths"]
        request_form['id'] = request.POST["id"]
        marksheet = MarksheetService()
        if request.POST["id"] != "":
            marksheet.update(request_form)
            message = 'marksheet updated successfully'
        else:
            marksheet.add(request_form)
            message = 'marksheet added successfully'
    return render(request, "Marksheet.html", {"message": message})


def marksheet_list(request):
    params = {}
    params['pageNo'] = 1
    params['pageSize'] = 5

    if request.method == "POST":

        if request.POST['operation'] == "search":
            params['name'] = request.POST['name']

        if request.POST['operation'] == "add":
            return redirect('/ORS/addMarksheet')

        if request.POST['operation'] == "next":
            params['pageNo'] = int(request.POST['pageNo'])
            params['pageNo'] += 1

        if request.POST['operation'] == "previous":
            params['pageNo'] = int(request.POST['pageNo'])
            params['pageNo'] -= 1

    marksheet = MarksheetService()
    marksheetList = marksheet.search(params);

    return render(request, "MarksheetList.html", {'marksheetList': marksheetList, 'pageNo': params['pageNo']})


def edit_marksheet(request, id):
    marksheet = MarksheetService()
    data = marksheet.get(id)
    return render(request, "Marksheet.html", {"form": data[0]})


def delete_marksheet(request, id):
    marksheet = MarksheetService()
    marksheet.delete(id)
    return redirect('/ORS/marksheetlist')
