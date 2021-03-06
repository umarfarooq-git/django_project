from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



def home(request):                 #Example of function based views.
    context={'posts': Post.objects.all() }
    return render(request, 'blog/home.html', context)

class postlistview(ListView):           #Example of class based views.
    model= Post
    template_name = 'blog/home.html'   # <app>/<model>_<viewpoint>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4            #number of post objects which should be shown per page


class userpostlistview(ListView):           #Example of class based views.
    model= Post
    template_name = 'blog/user-posts.html'   # <app>/<model>_<viewpoint>.html
    context_object_name = 'posts'
    paginate_by = 4            #number of post objects which should be shown per page

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailview(DetailView):
    model= Post

class PostCreateview(LoginRequiredMixin, CreateView):
    model= Post  
    fields=['title','content'] 
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)         # super() is used to run the save method of parent class.

class PostUpdateview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model= Post  
    fields=['title','content']
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteview(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model= Post
    success_url= '/' #this is another way to manage success url. / denotes the home page.

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    

    def get_success_url(self):
        return reverse('blog-home')
    
    
def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
# Create your views here.
