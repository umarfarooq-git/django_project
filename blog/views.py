from django.shortcuts import render
from .models import Post

posts= [
{   'author': 'umar farooq',
    'title': 'Post1',
    'content': 'first post content',
    'date_posted': '20 august 2021'

},
{
    'author': 'irfan yousaf',
    'title': 'Post2',
    'content': 'second post content',
    'date_posted': '12 july 2021'
}
]

def home(request):
    context={'posts': Post.objects.all() }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
# Create your views here.
