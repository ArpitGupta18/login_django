from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')


def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = first_name
        myuser.last_name = last_name

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('sign-in')

    return render(request, 'authentication/signup.html')


def sign_in(request):
    return render(request, 'authentication/signin.html')


def sign_out(request):
    pass
