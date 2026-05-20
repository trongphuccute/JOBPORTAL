from django.contrib import admin
from .models import BlogPost, Comment, Like



@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'total_likes', 'total_comments')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'content', 'author__username')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at', 'slug')
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('title', 'slug', 'author', 'content')
        }),
        ('Hình ảnh', {
            'fields': ('image',)
        }),
        ('Thời gian', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('created_at', 'post', 'user')
    search_fields = ('content', 'user__username', 'post__title')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')
    list_filter = ('created_at', 'post')
    search_fields = ('user__username', 'post__title')
    readonly_fields = ('created_at',)

