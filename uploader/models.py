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

    # TYPE_CHOICES = [
    #     ('Type1', 'type1'),
    #     ('Type2', 'type2'),
    #     ('Type3', 'type3'),
    # ]
    # type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    uploaded_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return str(self.writer_id)

# class File(models.Model):
#     # 파일 정보
#     # user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, verbose_name='작성자')
#     id = models.BigAutoField(help_text="File ID", primary_key=True)
#     file_tif = models.ForeignKey(UploadFile, verbose_name='파일원본', on_delete=models.CASCADE, related_name='file_tif', db_column="tif_file")
#     file_name = models.CharField(max_length=128, verbose_name='파일명')
#     threshold = models.ForeignKey('threshold.SetThreshold', on_delete=models.SET_DEFAULT, default=80, verbose_name='임계치')
#
#     RESULT_CHOICES = [
#         ('DANGER', '위험'),
#         ('SAFE', '안전'),
#     ]
#     result = models.CharField(null=True, max_length=10, choices=RESULT_CHOICES, verbose_name='결과', blank=True)
#
#     COMMIT_STATUS_CHOICES = [
#         ('WAIT', '분석대기'),
#         ('ONGO', '분석중'),
#         ('DONE', '분석완료'),
#     ]
#     commit_status = models.CharField(max_length=4, choices=COMMIT_STATUS_CHOICES, default='WAIT', verbose_name='상태')
#
#     def __str__(self):
#         return self.file_name
#
# class Page(models.Model):
#     id = models.BigAutoField(help_text="Page ID", primary_key=True)
#     # file = models.ForeignKey(UploadFile, verbose_name='파일', related_name="file_origin", on_delete=models.CASCADE, db_column="file")
#     filename = models.CharField(null=True, max_length=128)
#     page_num = models.PositiveIntegerField(verbose_name='페이지')
#     img_dir = models.TextField(blank=True, null=True, verbose_name='이미지')
#     box_json = models.CharField(null=True, max_length=128)
#     content = models.TextField(null=True, verbose_name='내용')
#     is_safe = models.BooleanField(null=True, verbose_name='안전여부', default=False)
#
#     def get_absolute_url(self):
#         return reverse('mysite:page_detail', kwargs={'pk':self.pk})
#
#     def __str__(self):
#         return self.id