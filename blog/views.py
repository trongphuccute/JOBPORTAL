from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Q
from .models import BlogPost, Comment, Like
from .forms import BlogPostForm, CommentForm


def blog_list(request):
    """Danh sách tất cả bài viết blog"""
    posts = BlogPost.objects.all()
    
    # Tìm kiếm
    search = request.GET.get('search', '')
    if search:
        posts = posts.filter(
            Q(title__icontains=search) | 
            Q(content__icontains=search) |
            Q(author__username__icontains=search)
        )
    
    # Lọc theo tác giả
    author_filter = request.GET.get('author', '')
    if author_filter:
        posts = posts.filter(author__username=author_filter)
    
    # Phân trang
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'posts': page_obj.object_list,
        'search': search,
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    """Chi tiết một bài viết"""
    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.comments.all()
    comment_form = CommentForm()
    
    # Kiểm tra user đã like chưa
    user_liked = False
    if request.user.is_authenticated:
        user_liked = Like.objects.filter(user=request.user, post=post).exists()
    
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'user_liked': user_liked,
    }
    return render(request, 'blog/blog_detail.html', context)


@login_required(login_url='login')
def create_blog_post(request):
    """Tạo bài viết blog mới"""
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Bài viết đã được tạo thành công!')
            return redirect('blog:blog_detail', slug=post.slug)
    else:
        form = BlogPostForm()
    
    context = {'form': form, 'action': 'Tạo bài viết'}
    return render(request, 'blog/blog_form.html', context)


@login_required(login_url='login')
def edit_blog_post(request, slug):
    """Chỉnh sửa bài viết blog"""
    post = get_object_or_404(BlogPost, slug=slug)
    
    # Kiểm tra quyền - chỉ tác giả hoặc admin mới có thể sửa
    if request.user != post.author and not request.user.is_staff:
        messages.error(request, 'Bạn không có quyền chỉnh sửa bài viết này!')
        return redirect('blog:blog_detail', slug=slug)
    
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bài viết đã được cập nhật!')
            return redirect('blog:blog_detail', slug=post.slug)
    else:
        form = BlogPostForm(instance=post)
    
    context = {'form': form, 'post': post, 'action': 'Chỉnh sửa bài viết'}
    return render(request, 'blog/blog_form.html', context)


@login_required(login_url='login')
def delete_blog_post(request, slug):
    """Xóa bài viết blog"""
    post = get_object_or_404(BlogPost, slug=slug)
    
    # Kiểm tra quyền
    if request.user != post.author and not request.user.is_staff:
        messages.error(request, 'Bạn không có quyền xóa bài viết này!')
        return redirect('blog:blog_detail', slug=slug)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Bài viết đã được xóa!')
        return redirect('blog:blog_list')
    
    context = {'post': post}
    return render(request, 'blog/blog_confirm_delete.html', context)


@login_required(login_url='login')
def add_comment(request, slug):
    """Thêm bình luận"""
    post = get_object_or_404(BlogPost, slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Bình luận đã được thêm!')
            return redirect('blog:blog_detail', slug=slug)
    
    return redirect('blog:blog_detail', slug=slug)


@login_required(login_url='login')
def delete_comment(request, comment_id):
    """Xóa bình luận"""
    comment = get_object_or_404(Comment, id=comment_id)
    post = comment.post
    
    # Kiểm tra quyền - chỉ tác giả comment hoặc admin mới có thể xóa
    if request.user != comment.user and not request.user.is_staff:
        messages.error(request, 'Bạn không có quyền xóa bình luận này!')
        return redirect('blog:blog_detail', slug=post.slug)
    
    comment.delete()
    messages.success(request, 'Bình luận đã được xóa!')
    return redirect('blog:blog_detail', slug=post.slug)


@login_required(login_url='login')
def like_post(request, slug):
    """Like/Unlike bài viết (AJAX)"""
    post = get_object_or_404(BlogPost, slug=slug)
    
    like_obj, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if not created:
        like_obj.delete()
        liked = False
    else:
        liked = True
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'liked': liked,
            'total_likes': post.total_likes()
        })
    
    return redirect('blog:blog_detail', slug=slug)


def my_posts(request):
    """Danh sách bài viết của user hiện tại"""
    if not request.user.is_authenticated:
        messages.error(request, 'Vui lòng đăng nhập!')
        return redirect('login')
    
    posts = BlogPost.objects.filter(author=request.user)
    
    # Phân trang
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'posts': page_obj.object_list,
    }
    return render(request, 'blog/my_posts.html', context)

