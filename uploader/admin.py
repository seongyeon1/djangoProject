from django.contrib import admin
from .models import UploadFile

class UploadFileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'file',
        'type',
        )
    search_fields = ('title',)

admin.site.register(UploadFile, UploadFileAdmin)