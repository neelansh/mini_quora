from django.conf.urls import url
from users.views import home, login

urlpatterns = [
    url(r'^$', home , name = "home"),
    url(r'^login$' , login , name= "login")
] 