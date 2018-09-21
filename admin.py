# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Organisation,OrganisationCorpusFund,OrganisationExpenditureLog,UserDonation,Profile,Donations_required


admin.site.register(Organisation)
admin.site.register(OrganisationCorpusFund)
admin.site.register(OrganisationExpenditureLog)
admin.site.register(UserDonation)
admin.site.register(Profile)
admin.site.register(Donations_required)
