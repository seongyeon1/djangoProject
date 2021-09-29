from django.db import models

import os
import uuid
from django.conf import settings
from django.db import models

class File(models.Model):
    # 파일 정보
    # user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name='작성자')
    id = models.BigAutoField(help_text="File ID", primary_key=True)
    # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_name = models.CharField(max_length=128, verbose_name='파일명')
    threshold = models.PositiveIntegerField(verbose_name='임계치', default=80)
    commit_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    description = models.TextField(verbose_name='설명')
    # result = models.CharField(max_length=10, verbose_name='결과')

    COMMIT_STATUS_CHOICES = [
        ('WAIT', '분석대기'),
        ('ONGO', '분석중'),
        ('DONE', '분석완료'),
    ]
    commit_status = models.CharField(max_length=4, choices=COMMIT_STATUS_CHOICES, default='WAIT', verbose_name='상태')

    def __str__(self):
        return self.file_name

class Page(models.Model):
    id = models.BigAutoField(help_text="Page ID", primary_key=True)
    file_id = models.ForeignKey("File", related_name="file", on_delete=models.CASCADE, db_column="file_id")
    is_safe = models.BooleanField(verbose_name='안전여부', default=False)
    box_json = models.CharField(max_length=128)
