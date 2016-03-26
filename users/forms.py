from django import forms
from users.models import MyUser

class login_form(forms.Form):
	username = forms.CharField(label = "Username" , max_length = 25)
	password = forms.CharField(label = "Password" , widget = forms.PasswordInput)