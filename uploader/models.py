# from django.core.validators import FileExtensionValidator
from django.db import models

class UploadFile(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    file = models.FileField(upload_to="upload/")
    description = models.TextField(null=True)

    TYPE_CHOICES = [
        ('Type1', 'type1'),
        ('Type2', 'type2'),
        ('Type3', 'type3'),
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    uploaded_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.title