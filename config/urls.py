from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('apps.core.urls')),
    path('blog/', include('apps.blog.urls')),
    path('support/', include('apps.support.urls')),
    path('robots.txt', lambda request: serve(request, 'robots.txt', document_root=settings.BASE_DIR), name='robots'),]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)