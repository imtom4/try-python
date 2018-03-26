//  http://campus.codeschool.com/courses/digging-into-django/level/1/section/2/the-detail-url

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^([0-9]+)/$', views.detail, name= 'detail')
]
