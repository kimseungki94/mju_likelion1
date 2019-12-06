from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blog = Blog.objects
    return render(request,'home.html',{'blog':blog})
def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.body = request.POST['body']
    blog.date = timezone.datetime.now()
    blog.save()
    return redirect('/blog' + str(blog.id))
def new(request):
    return render(request,'new.html')
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html',{'blog':blog_detail})
# Create your views here.
