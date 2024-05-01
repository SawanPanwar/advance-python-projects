from django.db import models


class Marksheet(models.Model):
    rollNo = models.IntegerField(max_length=20)
    name = models.CharField(max_length=30)
    physics = models.FloatField(max_length=3)
    chemistry = models.FloatField(max_length=3)
    maths = models.FloatField(max_length=3)

    class Meta:
        db_table = "SOS_MARKSHEET"


class RequestData(models.Model):
    http_remote_address = models.CharField(max_length=255)
    http_remote_host = models.CharField(max_length=255)
    http_remote_user = models.CharField(max_length=255)
    http_host = models.CharField(max_length=255)
    http_user_agent = models.CharField(max_length=255)

    class Meta:
        db_table = "SOS_REQUEST_DATA"
