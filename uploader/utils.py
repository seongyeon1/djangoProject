import os
from uuid import uuid4

# 파일이름을 uuid로 바꿔서 저장
def rename_file_to_uuid(instance, filename):
    upload_to = f'upload/'
    ext = filename.split('.')[-1]
    uuid = uuid4().hex

    if instance:
        filename = '{}_{}.{}'.format(uuid, instance, ext)

    return os.path.join(upload_to, filename)