from django.utils.text import slugify
import string
import random


def generate_unique_slug(title, model):
    """Tạo slug duy nhất nếu slug đã tồn tại"""
    slug = slugify(title)
    original_slug = slug
    counter = 1
    
    while model.objects.filter(slug=slug).exists():
        slug = f"{original_slug}-{counter}"
        counter += 1
    
    return slug


def truncate_text(text, length=100):
    """Rút gọn text"""
    if len(text) > length:
        return text[:length] + "..."
    return text


def get_popular_posts(limit=5):
    """Lấy bài viết phổ biến nhất"""
    from .models import BlogPost
    posts = BlogPost.objects.all()
    return sorted(posts, key=lambda x: x.total_likes(), reverse=True)[:limit]


def get_recent_posts(limit=5):
    """Lấy bài viết mới nhất"""
    from .models import BlogPost
    return BlogPost.objects.all()[:limit]
