from django.conf.urls import url
from . import views
from django.db import models
from  .models import ALBUMS

urlpatterns = [
    #url(r'^$', views.index ),
    #url(r'^admin/', admin.site.urls),
    url(r'^$', views.listing),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail),
    url(r'^search/$', views.search),
]