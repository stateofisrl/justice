from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('sitemap.xml', views.SitemapView.as_view(), name='sitemap'),]