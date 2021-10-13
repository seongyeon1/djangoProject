from django.urls import reverse

import os
import uuid
from django.conf import settings
from django.db import models

# class File(models.Model):
#     # 파일 정보
#     # user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name='작성자')
#     id = models.BigAutoField(help_text="File ID", primary_key=True)
#     # uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#
#     file_name = models.CharField(max_length=128, verbose_name='파일명')
#     threshold = models.PositiveIntegerField(verbose_name='임계치', default=80)
#     commit_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
#     description = models.TextField(verbose_name='설명')
#
#     RESULT_CHOICES = [
#         ('DANGER', '위험'),
#         ('SAFE', '안전'),
#     ]
#     result = models.CharField(max_length=10, choices=RESULT_CHOICES, verbose_name='결과', blank=True, null=True)
#
#     COMMIT_STATUS_CHOICES = [
#         ('WAIT', '분석대기'),
#         ('ONGO', '분석중'),
#         ('DONE', '분석완료'),
#     ]
#     commit_status = models.CharField(max_length=4, choices=COMMIT_STATUS_CHOICES, default='WAIT', verbose_name='상태', blank=True, null=True)
#
#     def __str__(self):
#         return self.file_name

class Page(models.Model):
    id = models.BigAutoField(help_text="Page ID", primary_key=True)
    #file = models.ForeignKey(UploadFile, verbose_name='파일', related_name="file", on_delete=models.CASCADE, db_column="file")
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)

    filename = models.CharField(null=True, max_length=128)
    page_num = models.PositiveIntegerField(verbose_name='페이지')
    img_dir = models.TextField(blank=True, null=True, verbose_name='이미지')
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')

    box_json = models.CharField(null=True, max_length=128)
    content = models.TextField(null=True, verbose_name='내용')
    is_safe = models.BooleanField(null=True, verbose_name='안전여부', default=False)

    def get_absolute_url(self):
        return reverse('mysite:page_detail', kwargs={'pk':self.pk})