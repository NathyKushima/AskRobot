from django.contrib import admin
from .models import Posts, Comment, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date', 'status')
    list_filter = ('categories', 'status')
    search_fields = ('title', 'description')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'post', 'created_at') 
    list_filter = ('created_at', 'author_name')
    search_fields = ('author_name', 'text')
