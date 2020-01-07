from django.contrib import admin
from django.conf.urls import url, include
#from django.urls import path
#from fastai.imports import *
from core.views import TestView 
from . import views

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^$', TestView.as_view(), name='test'),
    url('admin/', admin.site.urls)
   
]