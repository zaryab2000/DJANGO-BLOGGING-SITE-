from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
        	'date',
        	'title',
        	'article',
        	'public',
        	'image'
        ]
        labels = {
            'public': ('MAKE IT PUBLIC')
        }

        help_texts = {
            'public': ('BY DEFAULT, ARTICLE IS PRIVATE')
        }
