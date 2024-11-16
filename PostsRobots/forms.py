from django import forms
from .models import Posts

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'category', 'gold_trophies', 'silver_trophies', 'bronze_trophies', 'status', 'description', 'image']