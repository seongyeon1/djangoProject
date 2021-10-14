from django.contrib import admin
from .models import *

class FileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'filename',
        'threshold',
        'commit_date',
        'commit_status'
        )
    search_fields = ('file_name',)

class PageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'filename',
        'page_num',
        'is_safe',
        )
    search_fields = ('file_name',)

admin.site.register(Page, PageAdmin)
admin.site.register(File, FileAdmin)