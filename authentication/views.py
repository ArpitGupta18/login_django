from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')


def sign_up(request):
    return render(request, 'authentication/signup.html')


def sign_in(request):
    return render(request, 'authentication/signin.html')


def sign_out(request):
    pass
