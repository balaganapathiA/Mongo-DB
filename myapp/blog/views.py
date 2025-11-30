from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import logging
from .models import Post
# posts = [
#         {'title':'post1','content':'post 1 content'},
#         {'title':'post2','content':'post 2 content'},
#         {'title':'post3','content':'post 3 content'},
#         {'title':'post4','content':'post 4 content'},
#         ]
# Create your views here.
def home(request):
    return HttpResponse("Hello, World!")

def url_redirect(request):
    return redirect('new')  # use the URL *name* not the path

def redirected_page(request):
    return HttpResponse("url redirected succesfully")

def render_page(request):
    posts=Post.objects.all()
    return render(request,"index.html",{'posts':posts})

def detail_page(request,slug):
    # post_details = next((item for item in posts if item["id"] == id),None)
    try:
        post_details=Post.objects.get(slug=slug)
        related_posts  = Post.objects.filter(category = post_details.category).exclude(pk=post_details.id)
    except Post.DoesNotExist:
        raise Http404("404 Page")
    log = logging.getLogger("testing")
    log.debug(f'id {post_details} {id} of detail page')
    return render(request,"detail.html",{"post_details":post_details, 'related_posts':related_posts})