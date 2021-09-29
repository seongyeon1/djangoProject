from django.contrib import admin
from .models import Page, File

class FileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'file_name',
        'threshold',
        'commit_date',
        'commit_status'
        )
    search_fields = ('file_name',)

class PageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'is_safe',
        'file_id',
        )
    search_fields = ('file_name',)

admin.site.register(Page, PageAdmin)
admin.site.register(File, FileAdmin)