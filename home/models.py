from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models.signals import post_save

def current_date():
    return datetime.today().isoformat()

# Careers
class Careers(models.Model):
    full_name = models.CharField(max_length=100)
    position_choice = [
        ('Marketing', 'Marketing'),
        ('Sales', 'Sales'),
        ('Customer Service', 'Customer Service'),
    ]
    position = models.CharField(max_length=20, choices=position_choice)
    cv = models.FileField(upload_to='cv_uploads/', blank=True, null=True)
    message = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.full_name

# News
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    date = models.DateField(default=current_date)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __self__(self):
        return self.title