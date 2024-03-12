from django.shortcuts import render, redirect, get_object_or_404
from .forms import CareersForm
from django import forms
from django.contrib import messages
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def about_us(request):
    return render(request, 'home/more/about_us.html')

def careers(request):
    if request.method == 'POST':
        form = CareersForm(request.POST, request.FILES)
        # Save on database
        if form.is_valid():
            career_instance = form.save()
            messages.success(request, "Form submitted successfully. Thanks for applying!")
            return redirect('careers')
    else:
        form = CareersForm()
    return render(request, 'home/more/careers.html', {'form': form})

def news(request):
    # Shows all the posts
    posts = Post.objects.all()
    return render(request, 'home/more/news/news.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'home/more/news/post_detail.html', {'post': post})