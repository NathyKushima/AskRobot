from django.urls import path
from . import views 

urlpatterns = [
    path('', views.ListView, name='postlist'),
    path('details/<int:id>/', views.DetailView, name='details'),
    path('postcreate', views.CreateView, name='postcreate'),
    path('postupdate/<int:id>', views.UpdateView, name='postupdate'),
    path('delete/<int:id>', views.DeleteView, name='delete'),
    path('about/', views.post_about, name='about'),
]