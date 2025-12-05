from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import logging
from django.core.paginator import Paginator
from .models import Post,AboutUs

from .forms import ContactForm,RegisterForm
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
     # getting data from post model
    all_posts = Post.objects.all()

    # paginate
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    log = logging.getLogger("testing")
    log.debug(f'page_obj {page_obj}')
    return render(request,"index.html",{'posts':page_obj})

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

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger("TESTING")
        if form.is_valid():
            logger.debug(f'POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
            #send email or save in database
            success_message = 'Your Email has been sent!'
            return render(request,'contact.html', {'form':form,'success_message':success_message})
        else:
            logger.debug(f'Form validation failure {message}')
        return render(request,'contact.html', {'form':form, 'name': name, 'email':email, 'message': message})
    return render(request,'contact.html')
def about_page(request):
    about_content = AboutUs.objects.first()
    if about_content is None or not about_content.content:
        about_content="SOLLA ONNUM ILA"
    else:
        about_content=about_content.content
    return render(request,'about.html',{'about_content':about_content})

def register_page(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)

    return render(request,'register.html',{'form':form})