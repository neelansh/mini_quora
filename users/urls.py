from django.conf.urls import url
from users.views import *

urlpatterns = [
    url(r'^$', home , name = "home"),
    url(r'^login$' , login , name= "login"),
    url(r'^logout$' , logout , name = "logout"),
    url(r'^signup$' , signup , name = "signup"),
] 