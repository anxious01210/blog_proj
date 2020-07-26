from django.shortcuts import render
from django.contrib.auth.decorators import login_required # function-based
from django.contrib.auth.mixins import LoginRequiredMixin # class-based
from django.views.generic import (TemplateView, ListView, DetailView, CreateView,UpdateView,DeleteView)
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post

    # define how to grab the list, it (def get_queryset(self):) allows you to use django's ORM when dealing
    # with just generic views and ables you to add alittle bit costume touch to it.
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView): # Now you are inheriting methods from both classes
    # With mixins your are going to need the 2 below necessary attributes
    login_url = '/login/' # In case the user is not loged-in where the user should go? (here ==> '/login/')
    redirect_field_name = 'blog/post_detail.html' # Just saying to where to redirect the visitors
    form_class = PostForm
    model = post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('published_date')
