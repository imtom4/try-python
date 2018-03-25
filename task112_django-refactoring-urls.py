# Let's refactor our project URL dispatcher to have a separate URL dispatcher in our app. 
# At the same time, let's have an empty URL path go to our homepage instead of /home.

# TravelTracker/urls.py =
from django.conf.urls import include, url
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('main.urls')),
]

# main/urls.py =
from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.home)
]
