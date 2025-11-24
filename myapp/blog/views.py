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
        {'title':'post1','content':'post 1 content'},
        {'title':'post2','content':'post 2 content'},
        {'title':'post3','content':'post 3 content'},
        {'title':'post4','content':'post 4 content'},
        ]
    return render(request,"index.html",{'posts':posts})

def detail_page(request,id):
    return render(request,"detail.html")