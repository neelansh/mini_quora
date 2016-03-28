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
			
class signup_form(forms.ModelForm):
	password = forms.CharField(label = "Password" , widget = forms.PasswordInput)
	confirm_password = forms.CharField(label = "Conform Password" , widget = forms.PasswordInput)

	def clean_email(self):
		data_email = self.cleaned_data.get("email" , "")
		if(not data_email):
			raise forms.ValidationError("this field is required")
		if(MyUser.objects.filter(email = data_email).exists()):
			raise forms.ValidationError("email alreaady exists")
		return data_email

	def clean_confirm_password(self):
		password = self.cleaned_data.get("password" , "")
		confirm_password = self.cleaned_data.get("confirm_password" , "")
		if(password and confirm_password and not password == confirm_password):
			raise forms.ValidationError("passwords doesn't match")
		return confirm_password

	class Meta:
		model = MyUser
		fields = ["username" ,"email" , "first_name" , "last_name"]