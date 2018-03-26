#  http://campus.codeschool.com/courses/digging-into-django/level/1/section/2/the-detail-view

from django.shortcuts import render
from .models import Location

def home(request):
    locations = Location.objects.all()
    return render(request, 'home.html', {'locations': locations})

def detail(request, location_id):
    location = Location.objects.get(id=location_id)
    
