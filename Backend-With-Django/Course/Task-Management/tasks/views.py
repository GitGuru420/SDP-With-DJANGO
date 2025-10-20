from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the task management system project")

def contact(request):
    return HttpResponse("<h1 style='color: red'>This is our contact page</h1>")