# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext
from django.shortcuts import render_to_response
from donatelove.forms import*
from django import forms
from .forms import RegistrationForm

def home(request):
    text = """<h1>welcome to donateloveapp!</h1>"""
    return HttpResponse(text)


def landing_page(request):
    # import pdb; pdb.set_trace()
    return render(request,'donatelove/home.html', {})

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(request,'organisation_listpage.html')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect(request,'landing_page.html')



def user_profilepage(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user_profilepage.html', {'profile_user': user})

def register_page(request):
    form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
    if form.is_valid():
        user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
        return HttpResponseRedirect('/')

    return render_to_response('registration/register.html',{},variables)



def organisationdetail_page(request, username):
    user = get_object_or_404(User,username=username)
    return render(request,'organisation_detailpage.html')

# def donation_page(request,username):
#     user = get_object_or_404(user,username=username)
#     return render(request,'make_payment.html')
#
