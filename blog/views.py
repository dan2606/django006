from django.shortcuts import render
from .models import Blog

# Create your views here.
def allblogs(request):
    blogs=Blog.objects.all
    return render(request,"blog/allblog.html",{"blogs":blogs})