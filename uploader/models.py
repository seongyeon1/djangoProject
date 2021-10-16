from django.core.validators import FileExtensionValidator
from django.conf import settings
from django.db import models

from uploader.utils import rename_file_to_uuid

class UploadFile(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    file = models.FileField(null=True, blank=True, upload_to=rename_file_to_uuid, validators=[FileExtensionValidator(allowed_extensions=['tif','jpeg'])])
    description = models.TextField(null=True)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    uploaded_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return str(self.writer_id)