from django.conf.urls import url , include
from .views import *


urlpatterns = [
    url(r'^create_ques/$' , create_ques),
]
