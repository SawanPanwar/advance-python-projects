from django.db import models


class Marksheet(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=50)
    physics = models.FloatField()
    chemistry = models.FloatField()
    maths = models.FloatField()
