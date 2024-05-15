from django.db import models


class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "SOS_USER"


class Marksheet(models.Model):
    rollNo = models.IntegerField(max_length=20)
    name = models.CharField(max_length=30)
    physics = models.FloatField(max_length=3)
    chemistry = models.FloatField(max_length=3)
    maths = models.FloatField(max_length=3)

    class Meta:
        db_table = "SOS_MARKSHEET"


class Files(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    class Meta:
        db_table = "SOS_FILES"
