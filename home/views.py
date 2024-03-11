from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def about_us(request):
    return render(request, 'home/more/about_us.html')

def careers(request):
    return render(request, 'home/more/careers.html')

def news(request):
    return render(request, 'home/more/news.html')