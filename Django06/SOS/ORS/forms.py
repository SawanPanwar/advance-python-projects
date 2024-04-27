from django.forms import ModelForm
from .models import Marksheet
from django import forms


class MarksheetForm(ModelForm):
    class Meta:
        model = Marksheet
        fields = "__all__"
        widgets = {
            "rollNo": forms.NumberInput(attrs={"placeholder": "Enter Rollno"}),
            "name": forms.TextInput(attrs={"placeholder": "Enter Name"}),
            "physics": forms.NumberInput(attrs={"placeholder": "Enter Physics Score"}),
            "chemistry": forms.NumberInput(attrs={"placeholder": "Enter Chemistry Score"}),
            "maths": forms.NumberInput(attrs={"placeholder": "Enter Maths Score"}),
        }
