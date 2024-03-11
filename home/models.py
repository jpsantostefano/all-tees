from django.db import models

# Create your models here.

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