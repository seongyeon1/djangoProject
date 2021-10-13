from django.contrib import admin
from .models import *

class UploadFileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'writer',
    )
    search_fields = ('title', 'writer', 'title')

admin.site.register(UploadFile, UploadFileAdmin)
# admin.site.register(Page)
# admin.site.register(File)