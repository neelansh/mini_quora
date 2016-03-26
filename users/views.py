from django.shortcuts import render,redirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.http import HttpResponse
from .forms import login_form
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

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
			user = f.authenticated_user
			auth_login(request , user)
			return redirect("/users/")
		else:
			return render(request , "users/login_form.html" , {"f" : f})


@require_GET
@login_required
def home(request):
	return redirect("/questions/all")
