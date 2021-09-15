from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Category
from .forms import AddCategoryForm, CreateArticleForm, UpdateArticleForm

# Create your views here.
def index(request):
    search= Article.objects.all()
    categories= Category.objects.all()

    title= None
    if 'search_name' in request.GET:
        title= request.GET['search_name']
        if title:
            search= search.filter(title__icontains= title)

    return render(request, 'main/index.html', {'article':search, 'categories':categories})


def details(request, detail_slug):
    post= get_object_or_404(Article, slug= detail_slug)
    return render(request, 'main/post_details.html', {'post':post})


def category(request, category_slug):
    category= get_object_or_404(Category, slug= category_slug)
    post_list= Article.objects.filter(category= category)
    return render(request, 'main/categories.html', {'post_list':post_list})


def add_category(request):
    if request.method == 'POST':
        form= AddCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form= AddCategoryForm()

    return render(request, 'main/add_category.html', {'form':form})


def add_post(request):
    if request.method == 'POST':
        form= CreateArticleForm(request.POST, request.FILES)
        if form.is_valid():
            myform= form.save(commit= False)
            myform.author= request.user
            myform.save()
            return redirect('/')
    else:
        form= CreateArticleForm()

    return render(request, 'main/add_post.html', {'form':form})


def update_post(request, update_slug):
    post= Article.objects.get(slug= update_slug)
    if request.method == 'POST':
        form= UpdateArticleForm(request.POST, request.FILES, instance= post)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form= UpdateArticleForm(instance= post)

    return render(request, 'main/update_post.html', {'form':form})


def delete_post(request, delete_slug):
    post= get_object_or_404(Article, slug= delete_slug)
    if request.method == 'POST':
        post.delete()
        return redirect('/')

    return render(request, 'main/delete_post.html', {'post':post})
