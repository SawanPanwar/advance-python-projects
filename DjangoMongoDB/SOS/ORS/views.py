from django.shortcuts import render
from django.http import HttpResponse

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client['django_mongo']
user_collection = db["User"]


def add_user(request):
    user1 = {"id": 3,
             "name": "narendra",
             "address": "Indore"}
    user_collection.insert_one(user1)
    return HttpResponse("Record Inserted")


def getAllUser(request):
    # Read the documents
    user_list = user_collection.find()
    return HttpResponse(user_list)


# Update one document
def update_user(request):
    update_data = user_collection.update_one({'id': int(1)}, {'$set': {'name': 'prashant'}})
    return HttpResponse("user Updated")


def delete_user(request):
    # Delete one document
    delete_user = user_collection.delete_one({'id': 2})
    return HttpResponse("UserDeleted ")
