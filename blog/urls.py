from django.urls import path
from . import views
from .views import PostCreateview, postlistview, PostDetailview, PostUpdateview, PostDeleteview, userpostlistview

urlpatterns =[
    path('', postlistview.as_view(), name='blog-home'),
    path('post/<str:username>', userpostlistview.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailview.as_view(), name='post-detail'),
    path('post/new/', PostCreateview.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateview.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteview.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]

# Either follow the template naming conention or metion the template address at views.py in repective class.