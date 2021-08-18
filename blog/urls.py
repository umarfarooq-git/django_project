from django.urls import path
from . import views
from .views import PostCreateview, postlistview, PostDetailview, CreateView

urlpatterns =[
    path('', postlistview.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailview.as_view(), name='post-detail'),
    path('post/new/', PostCreateview.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]