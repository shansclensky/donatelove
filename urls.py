from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login
from django.contrib.auth import views as auth_views
from donatelove.views import (
    home,
    landing_page,
    user_profilepage,
    logout_page,
    register_page_main,
    organisation_detailpage,
    my_view,
    organisation_listpage,
    payment_page,

)

urlpatterns = [
    url(r'^$', landing_page,name='landing_page'),
    url(r'^user_profile/$', user_profilepage,name='user_profile'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout_page,name='logout'),
    url(r'^register_page_main/$', register_page_main,name= 'register'),
    url(r'^my_view/$',my_view,name='my_view'),
    url(r'^organisation_detailpage/(?P<id>[0-9]+)/$',organisation_detailpage,name ='org_det'),
    url(r'^organisation_listpage/$',organisation_listpage,name='org_list'),
    url(r'^payment_page/$',payment_page,name='payment')
]
