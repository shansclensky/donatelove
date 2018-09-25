# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from donatelove.forms import*
from django import forms
from donatelove.forms import (
    UserCreationForm,
    ProfileForm,
)

from donatelove.models import (
    Organisation,
)


def home(request):
    text = """<h1>welcome to donateloveapp!</h1>"""
    return HttpResponse(text)


def landing_page(request):
    return redirect(reverse('org_list'))


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(request,'donatelove/organisation_listpage.html')


def logout_page(request):
    logout(request)
    return redirect(reverse('login'))


@login_required(login_url='/donatelove/login/')
def organisation_listpage(request):
    organisations = Organisation.objects.all()
    context = {
        'organisations': organisations,
    }
    return render(request, 'donatelove/organisation_listpage.html', context)

def user_profilepage(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'donatelove/user_profilepage.html', {'profile_form': form})


def register_page_main(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'User_Creation_Form': form})


def organisation_detailpage(request, id):
    org = Organisation.objects.get(id=id)
    return render(request,'donatelove/organisation_detailpage.html', {'org': org})
