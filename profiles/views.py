from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

# Create your views here.

def home(request):

    return render(request, 'base.html')

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        bio = request.POST['bio']

        new_profile = Profile(name=name, email=email, bio=bio)
        new_profile.save()
        success= 'User '+ name +' Created Successfully'
        return HttpResponse(success)

