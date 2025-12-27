from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template.loader import render_to_string
from apps.blog.models import BlogPost
from .models import ContactMessage


class HomeView(View):
    def get(self, request):
        latest_posts = BlogPost.objects.filter(published=True).order_by('-created_at')[:3]
        context = {
            'latest_posts': latest_posts,
        }
        return render(request, 'core/index.html', context)

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            
            if name and email and message:
                ContactMessage.objects.create(
                    name=name,
                    email=email,
                    message=message
                )
                return render(request, 'core/index.html', {
                    'message_sent': True,
                    'latest_posts': BlogPost.objects.filter(published=True).order_by('-created_at')[:3]
                })
        
        return render(request, 'core/index.html', {
            'latest_posts': BlogPost.objects.filter(published=True).order_by('-created_at')[:3]
        })


class SitemapView(View):
    def get(self, request):
        posts = BlogPost.objects.filter(published=True)
        context = {
            'posts': posts,
        }
        xml = render_to_string('sitemap.xml', context, request=request)
        return HttpResponse(xml, content_type='application/xml')
