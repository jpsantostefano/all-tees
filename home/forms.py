from django import forms
from .models import Careers

class CareersForm(forms.ModelForm):
    class Meta:
        model = Careers
        fields = ['full_name', 'email', 'position', 'message', 'cv']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'cv': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }