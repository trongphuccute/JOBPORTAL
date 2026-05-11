from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Blog posts
    path('', views.blog_list, name='blog_list'),
    path('post/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('create/', views.create_blog_post, name='create_post'),
    path('post/<slug:slug>/edit/', views.edit_blog_post, name='edit_post'),
    path('post/<slug:slug>/delete/', views.delete_blog_post, name='delete_post'),
    
    # Comments
    path('post/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    
    # Likes
    path('post/<slug:slug>/like/', views.like_post, name='like_post'),
    
    # User's posts
    path('my-posts/', views.my_posts, name='my_posts'),
]
