from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myview(request):
    return render(request,'myapp/index.html')

def practicevioew(request):
    return render(request,'myapp/practice.html')

# def name(request):
#     name="Vidyashree"
#     age=22
#     print(name, age)
#     return HttpResponse(name)
