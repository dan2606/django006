from django.shortcuts import render
from . import models
# Create your views here.

def home(request):
    jobs=models.Job.objects.all
    print(jobs)
    return render(request, "jobs/home.html", {"jobs": jobs})