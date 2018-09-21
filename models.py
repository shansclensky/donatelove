# from django.contrib.auth.models import UserDonation
from decimal import Decimal
from django.db import models
from django.contrib.auth.models import User
# from django.contrib import admin

#user profile along with a smallbio
class Profile(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE,default="")
    email = models.EmailField(max_length=70,blank=True)
    user_bio = models.TextField(null=True)
    # avatar = models.ImageField()
    is_organisation = models.BooleanField()

class Donations_required(models.Model):
    #organisation name and detail along with required money
    name = models.CharField(max_length=100,default="")
    detail = models.TextField(blank=True , null =True)
    Money_required = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))


#organisation detail along with corpus fund is specified
class Organisation(models.Model):
    # admin = models.ManyToManyField(admin,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default="")
    detail = models.TextField(blank=True, null=True)
    corpus_fund = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
    def __str__(self):
        return self.name


#organisation corpus fund along with its organisation name is listed to the registered user
class OrganisationCorpusFund(models.Model):
    organisation = models.OneToOneField(Organisation,on_delete=models.CASCADE,default="")
    amount = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))

#The organisation expenditure with previous and recent transactions is listed
class OrganisationExpenditureLog(models.Model):
    organisation = models.ForeignKey(Organisation,on_delete=models.CASCADE,default="")
    amount = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))

class UserDonation(models.Model):
    user = models.ForeignKey(User,default="")
    organisation = models.ForeignKey(Organisation,on_delete=models.CASCADE,default="")
    amount = models.DecimalField(max_digits=20,decimal_places=4,default=Decimal('0.0000'))
