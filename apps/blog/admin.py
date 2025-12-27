from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, BlogPost, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(BlogPost)
class BlogPostAdmin(SummernoteModelAdmin):
    list_display = ['title', 'author', 'category', 'published', 'created_at']
    list_filter = ['published', 'category', 'created_at']
    search_fields = ['title', 'body', 'meta_keywords']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body',)
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category', 'author', 'published')
        }),
        ('Content', {
            'fields': ('excerpt', 'body', 'cover_image', 'tags')
        }),
        ('SEO Settings', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author_name', 'post', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['author_name', 'author_email', 'content']
    readonly_fields = ['created_at']
