from django import forms
from users.models import MyUser
from django.contrib.auth import authenticate

class login_form(forms.Form):
	username = forms.CharField(label = "Username" , max_length = 25)
	password = forms.CharField(label = "Password" , widget = forms.PasswordInput)

	def clean_username(self):
		data_username = self.cleaned_data.get("username" , "")
		if(MyUser.objects.filter(username = data_username).count() != 1):
			raise forms.ValidationError("invalid username")
		return data_username

	def clean(self):
		data_username = self.cleaned_data.get("username" , "")
		data_password = self.cleaned_data.get("password" , "")
		if(data_username and data_password and not authenticate(username = data_username , password = data_password)):
			raise forms.ValidationError("username and password does not match")
		return self.cleaned_data
			