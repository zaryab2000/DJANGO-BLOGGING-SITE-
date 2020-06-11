import requests
import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.models import User
from django.db.models import Sum
from blog.models import Post


# FUNCTION TO REGISTER NEW USERS

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            '''VALIDATING CAPTCHA'''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }

            r = requests.post(url, data = values)
            response = json.loads(r.text)
            verify = response['success']
            if verify:
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect('login')
            else:
                messages.warning(request, 'INVALID CAPTCHA')
                return redirect('register')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


