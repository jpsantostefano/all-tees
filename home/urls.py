from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('careers/', views.careers, name='careers'),
    path('news/', views.news, name='news'),
]