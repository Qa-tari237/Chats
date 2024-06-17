from django.contrib import admin
from django.contrib.admin import AdminSite

# Register your models here.
from .models import Omboli_Room, OmboliMessage

admin.site.register(Omboli_Room)

admin.site.register(OmboliMessage)


"""class Chatadmin(AdminSite):
    site_header = 'Omboli Chat Admin'
    site_title = 'Omboli Chat Admin'
    index_title = 'Omboli Chat Admin'


    def index(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['recent_entries'] = Chatadmin.objects.order_by('-created_at')[:5]
        return super().index(request, extra_context)

admin_site = Chatadmin(name='admin')

@admin.register(Chatadmin, site=admin_site)
class ChatadminAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content')"""