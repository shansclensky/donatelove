from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist





class ProfileForm(forms.ModelForm):
    old_password = forms.CharField(label=("Old password"))
    new_password1 = forms.CharField(label=("new password1"))
    new_password2 = forms.CharField(label=("new password2"))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','old_password', 'new_password1', 'new_password2')



    def clean_password2(self):
       if new_password1 and new_password2 and new_password1 != new_password2:
           raise forms.ValidationError('password_mismatch')
       return new_password2

    def save(self, commit=True):
        user = super(ProfileForm,self).save(commit=False)
        user.set_password(self.cleaned_data["new_password1"])
        if commit:
            user.save()
        return user




class UserCreationForm(forms.ModelForm):
     password1 = forms.CharField(label=("Password"))
     password2 = forms.CharField(label=("Password confirmation"))
     class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

     def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('password_mismatch')
        return password2

     def save(self, commit=True):
         user = super(UserCreationForm,self).save(commit=False)
         user.set_password(self.cleaned_data["password1"])
         if commit:
             user.save()
         return user
