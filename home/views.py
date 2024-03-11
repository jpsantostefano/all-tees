from django.shortcuts import render
from .forms import CareersForm
from django import forms
from django.contrib import messages

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
    return render(request, 'home/more/news.html')