from django.shortcuts import render,redirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout, login as auth_login , authenticate
from .models import MyUser

# Create your views here.
@require_http_methods([ "GET" , "POST"])
def login(request):
	if request.user.is_authenticated():
		return redirect(reverse("home"))
	if(request.method == "GET"):
		f = login_form()
		context = { "f" : f }
		return render(request , "users/login_form.html" , context)
	else:
		f = login_form(request.POST)
		if(f.is_valid()):
			user = authenticate(username = f.cleaned_data["username"] , password = f.cleaned_data["password"])
			auth_login(request , user)
			return redirect("/users/")
		else:
			return render(request , "users/login_form.html" , {"f" : f})


@require_GET
@login_required
def home(request):
	context = {"user" : request.user.username}
	return render(request , "users/home_template.html" , context)

@require_GET
@login_required
def logout(request):
	auth_logout(request)
	return render(request , "users/logout.html")

@require_http_methods([ "POST" , "GET" ])
def signup(request):
	if(request.user.is_authenticated()):
		return redirect(reverse("home"))
	if(request.method == "GET"):
		f = signup_form()
		return render(request , "users/signup_form.html" , {"f" : f})
	else:
		f = signup_form(request.POST)
		if(not f.is_valid()):
			return render(request , "users/signup_form.html" , {"f" : f})
		else:
			new_user = f.save(commit = False)
			new_user.set_password(f.cleaned_data.get('password'))
			new_user.save()
			return redirect(reverse("login"))