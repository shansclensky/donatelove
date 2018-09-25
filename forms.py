from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

# from django.contrib.auth.models import User



class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')



#
# class RegistrationForm(forms.ModelForm):
#
#     class Meta:
#         model =
#         fields = ('first_name','last_name','password1','password2')

class UserCreationForm(forms.ModelForm):
     password1 = forms.CharField(label=("Password"))
     password2 = forms.CharField(label=("Password confirmation"))
     class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

     def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2



# class RegistrationForm(forms.Form):
#     username = forms.CharField(label='username', max_length=30)
#     email = forms.EmailField(label='Email')
#     password1 = forms.CharField(label='Password',
#                           widget=forms.PasswordInput())
#     password2 = forms.CharField(label='Password (Again)',
#                         widget=forms.PasswordInput())
#     def clean_password2(self):
#         if 'password1' in self.cleaned_data:
#             password1 = self.cleaned_data['password1']
#             password2 = self.cleaned_data['password2']
#             if password1 == password2:
#                 return password2
#         raise forms.ValidationError('Passwords do not match.')
#
#     def clean_username(self):
#         username = self.cleaned_data['username']
#         if not re.search(r'^\w+$', username):
#             raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
#         try:
#             User.objects.get(username=username)
#         except ObjectDoesNotExist:
#             return username
#         raise forms.ValidationError('Username is already taken.')
