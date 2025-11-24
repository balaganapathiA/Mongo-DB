from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello, World!")

def url_redirect(request):
    return redirect('new')  # use the URL *name* not the path

def redirected_page(request):
    return HttpResponse("url redirected succesfully")

def render_page(request):
    posts = [
     
        ]
    return render(request,"index.html",{'posts':posts})
