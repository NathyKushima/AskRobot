from django.contrib import admin
from .models import Posts, Comment

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'post_date', 'status')
    list_filter = ('category', 'status')
    search_fields = ('title', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'post', 'created_at') 
    list_filter = ('created_at', 'author_name')
    search_fields = ('author_name', 'text')
