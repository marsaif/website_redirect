from django.contrib import admin
from .models import UrlRedirect


class UrlRedirectAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'url', 'clicks', 'updated_at')
    list_filter = ('job_id',)
    search_fields = ('job_id', 'url')
    readonly_fields = ('clicks',)


admin.site.register(UrlRedirect, UrlRedirectAdmin)
