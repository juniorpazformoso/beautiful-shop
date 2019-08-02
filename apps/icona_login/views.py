from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.messages import info, error
from django.utils.translation import ugettext_lazy as _


def register_user(request):
    """
    Create new user
    """
    if request.method == "POST":
        user = User()
        user.username = request.POST.get('email')
        user.email = request.POST.get('email')
        user.password = make_password(request.POST.get('password'))
        user.save()

        info(request, _("The user was created successfully."))

        return redirect('login_user')

    return render(request, 'icona_login/register_user.html')


def login_user(request):
    """
    Login user
    """
    if request.method == "POST":

        user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))

        if user:
            login(request, user)

            return redirect('home')


    return render(request, 'icona_login/login_user.html')
