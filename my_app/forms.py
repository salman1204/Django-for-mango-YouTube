from django import forms
from my_app import models

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.students
        fields = "__all__"
