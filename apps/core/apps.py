from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'    
    def ready(self):
        from django.contrib import admin
        admin.site.site_header = "ScamResolvedCSI Administration"
        admin.site.site_title = "ScamResolvedCSI Admin"
        admin.site.index_title = "Welcome to ScamResolvedCSI Admin Panel"