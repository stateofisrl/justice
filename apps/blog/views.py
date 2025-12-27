from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from .models import BlogPost, Category, Comment


class BlogListView(View):
    def get(self, request):
        posts = BlogPost.objects.filter(published=True).order_by('-created_at')
        category_slug = request.GET.get('category')
        
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            posts = posts.filter(category=category)
        
        categories = Category.objects.all()
        
        paginator = Paginator(posts, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            'page_obj': page_obj,
            'categories': categories,
            'selected_category': category_slug,
        }
        return render(request, 'blog/blog_list.html', context)


class BlogDetailView(View):
    def get(self, request, slug):
        post = get_object_or_404(BlogPost, slug=slug, published=True)
        approved_comments = post.comments.filter(status='approved')
        
        context = {
            'post': post,
            'comments': approved_comments,
            'comment_form': None,
        }
        return render(request, 'blog/blog_detail.html', context)

    def post(self, request, slug):
        post = get_object_or_404(BlogPost, slug=slug, published=True)
        
        author_name = request.POST.get('author_name')
        author_email = request.POST.get('author_email')
        content = request.POST.get('content')
        
        if author_name and author_email and content:
            Comment.objects.create(
                post=post,
                author_name=author_name,
                author_email=author_email,
                content=content
            )
        
        approved_comments = post.comments.filter(status='approved')
        context = {
            'post': post,
            'comments': approved_comments,
            'comment_submitted': True,
        }
        return render(request, 'blog/blog_detail.html', context)
