from django import forms
from .models import Posts, Comment

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'category', 'gold_trophies', 'silver_trophies', 'bronze_trophies', 'status', 'description', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'text']
        labels = {
            'author_name': 'Your Name (Optional)',
            'text': 'Comment',
        }