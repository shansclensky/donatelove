from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth import views as auth_views
from donatelove.views import (
    home,
    landing_page,
    user_profilepage,
    logout_page,
    register_page,
    organisationdetail_page,
    my_view,
)

urlpatterns = [
    url(r'^$', landing_page,name='landing_page'),
    url(r'^user/(\w+)/$', user_profilepage,name='user_profile'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout_page,name='logout'),
    url(r'^register/$', register_page,name= 'register'),
    url(r'^my_view/$',my_view,name='my_view'),
    url(r'^organisationdetail_page/$',organisationdetail_page,name ='org_det')
]
