from django import forms
from .models import Food

class NewBlog(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['title', 'body']