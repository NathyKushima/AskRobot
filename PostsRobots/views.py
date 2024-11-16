from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Posts
from .forms import PostsForm

def post_about(request):
    return render(request, 'PostsRobots/about.html')

def ListView(request):
    template_name = 'PostsRobots/postlist.html' 
    posts = Posts.objects.all() 
    context = {     
        'posts': posts
        }
    return render(request, template_name, context)

def DetailView(request, id):
    template_name = 'PostsRobots/details.html'
    post = get_object_or_404(Posts, id=id)
    context = {
        'post': post
    }
    return render(request, template_name, context)

def CreateView(request):
    if request.method == 'POST': 
        form = PostsForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form = form.save(commit=False)
            form.save() 
            
            messages.success(request, 'O post foi criado com sucesso') 
            return HttpResponseRedirect(reverse('postlist')) 
        
    form = PostsForm() 
    return render(request, 'PostsRobots/postform.html', {"form": form})

def UpdateView(request, id):
    post = get_object_or_404(Posts, id=id)
    form = PostsForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()

        messages.success(request, 'O post foi atualizado com sucesso')
        return HttpResponseRedirect(reverse('details', args=[post.id]))
    
    return render(request, 'PostsRobots/postform.html', {"form": form})

def DeleteView(request, id):
    post = Posts.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'O post foi deletado com sucesso')
        return HttpResponseRedirect(reverse('postlist'))
    return render(request, 'PostsRobots/delete.html')