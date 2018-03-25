from django.conf.urls import url
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home)
]

# main/views.py =
# from django.http import HttpResponse
# def home(request):
#    return HttpResponse('Welcome Home Travelers!') 
