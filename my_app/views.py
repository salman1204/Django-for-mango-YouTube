from django.shortcuts import render
from django.http import HttpResponse
from .models import students 
from my_app import forms


# Create your views here.

def home(request):
    students_list = students.objects.order_by('name')
    diction = {'students': students_list}
    return render(request, 'my_app/index.html', context=diction)
   

def form(request):
    new_form = forms.StudentForm()

    if request.method == "POST":
        new_form = forms.StudentForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return home(request)

    diction = {'test_form': new_form}
    return render(request, 'my_app/form.html', context=diction)
