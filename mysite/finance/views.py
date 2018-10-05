from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home2(request):
    return HttpResponse("Hello World, Welcome to index page")
def menu2(request):
    return HttpResponse("Welcome to menu page")
def login2(request):
    return HttpResponse("Welcome to login page")
def content2(request):
    return render(request, 'finance/home.html', {})