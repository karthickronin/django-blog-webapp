from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Post, AboutUs
import logging
from django.core.paginator import Paginator
from .forms import ContactForm, RegisterForm
# posts = [
#             {'id':1,'title':"Post 1","content":"Content of Post 1"},
#             {'id':2,'title':"Post 2","content":"Content of Post 2"},
#             {'id':3,'title':"Post 3","content":"Content of Post 3"},
#             {'id':4,'title':"Post 4","content":"Content of Post 4"}
#     ]
# Create your views here.
def index(request):
    blog_title = "Latest Posts"
    posts = Post.objects.all()
    paginator = Paginator(posts,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'blog/index.html',{'blog_title': blog_title,'page_obj': page_obj})

def detail(request, slug):
    # post = next((item for item in posts if item['id']==int(post_id)),None)
    # logger = logging.getLogger("TESTING")
    # logger.debug(f"Post variable is {post}")
    post = Post.objects.get(slug=slug)
    related_posts = Post.objects.filter(category=post.category).exclude(pk=post.id)
    return render(request,'blog/detail.html',{"post":post,"related_posts":related_posts})

def contact(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            
            logger = logging.getLogger("TESTING")
            if form.is_valid():
                logger.debug(f"Post Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
                success_msg = "Your Email has been sent!"
                return render(request,'blog/contact.html',{'success_msg':success_msg})
            else:
                logger.debug("Form validation failure ...")
            return render(request,'blog/contact.html', {'form':form, 'name': name, 'email': email, 'message': message})                 
        return render(request,'blog/contact.html')

def about(request):
     about_content = AboutUs.objects.first()
     if about_content is None or not about_content.content:
          about_content = "Default content goes here ..."
     else:
          about_content = about_content.content
     return render(request, 'blog/about.html',{'about_content':about_content})

def register(request):
     form = RegisterForm()
     if request.method == "POST":
          form = RegisterForm(request.POST)
          if form.is_valid():
               user = form.save(commit=False)
               print('Register Success!')
               user.set_password(form.cleaned_data['password'])
               user.save()
     return render(request,'blog/register.html',{'form':form})
