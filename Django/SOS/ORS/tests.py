from django.test import TestCase

from .models import User


class TestModel(TestCase):
    form = User(firstName="Shyammm", lastName="Sharma", email="Shyam@gmail.com", password="1234")
    form.save()
    print("Data Saved") #py manage.py test.py

