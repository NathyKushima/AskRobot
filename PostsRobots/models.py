from django.db import models
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Posts(models.Model):
    STATUS_CHOICES = [
        ('active', 'Ativo'),
        ('retired', 'Aposentado'),
        ('undefined', 'Indefinido'),
    ]

    title = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category, related_name="posts")
    gold_trophies = models.IntegerField(default=0, help_text="Number of gold trophies")
    silver_trophies = models.IntegerField(default=0, help_text="Number of silver trophies")
    bronze_trophies = models.IntegerField(default=0, help_text="Number of bronze trophies")    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='undefined')
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
User = get_user_model()

class Comment(models.Model):
    author_name = models.CharField(max_length=100, blank=True, null=True, default="Anonymous")
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.author_name:
            self.author_name = "Anonymous"
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.author_name or "Anonymous"} - {self.text[:30]}'