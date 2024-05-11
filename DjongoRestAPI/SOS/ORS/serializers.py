from .models import Marksheet
from rest_framework import serializers


class MarksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marksheet
        fields = ('rollno',
                  'name',
                  'physics',
                  'chemistry',
                  'maths')
