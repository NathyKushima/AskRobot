from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Posts, Comment, Category
from .forms import PostsForm, CommentForm

def category_list_view(request):
    categories = Category.objects.all()
    return render(request, 'PostsRobots/category_list.html', {'categories': categories})

def category_detail_view(request, id):
    category = get_object_or_404(Category, id=id)
    posts = category.posts.all()
    return render(request, 'PostsRobots/category_detail.html', {'category': category, 'posts': posts})

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
            post = form.save(commit=False)
            form.save_m2m() 
            post.save()
            
            messages.success(request, 'O post foi criado com sucesso') 
            return HttpResponseRedirect(reverse('postlist')) 
        
    form = PostsForm() 
    return render(request, 'PostsRobots/postform.html', {"form": form})

def UpdateView(request, id):
    post = get_object_or_404(Posts, id=id)
    form = PostsForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        form.save_m2m()  # Salva as relações ManyToMany
        post.save()

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

def DetailView(request, id):
    template_name = 'PostsRobots/details.html'
    post = get_object_or_404(Posts, id=id)
    comments = post.comments.all()
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, template_name, context)

def add_comment(request, id):
    post = get_object_or_404(Posts, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if not comment.author_name:
                comment.author_name = "Anonymous"
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('details', args=[id]))
    else:
        form = CommentForm()
    return render(request, 'PostsRobots/comment_form.html', {'form': form, 'post': post})