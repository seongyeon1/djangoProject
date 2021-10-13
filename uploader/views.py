from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import FormView

from django.conf import settings
from django.core.files.storage import default_storage

from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import os, glob, cv2

from .forms import UploadFileForm
from .models import UploadFile
from mysite.models import *

import pytesseract  # ======= > Add

try:
    from PIL import Image
except:
    import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 파일 업로드 (tif 확장자만 허용)
@login_required
@csrf_exempt
def uploadfile(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        file = request.FILES['file']

        uploadfile = UploadFile(
            title=title,
            description=description,
            file=file,
            writer=request.user,
        )
        uploadfile.save()

        file_dir = file.temporary_file_path()
        filename = os.path.basename(file_dir).split('.')[0]

        ret, images = cv2.imreadmulti(file_dir, [], cv2.IMREAD_ANYCOLOR)
        for idx, img in enumerate(images):
            # 페이지 이미지 저장하기
            cv2.imwrite(f'static/upload/{filename}_{idx + 1}.jpg', img)
            # 페이지 이미지 열기
            img = Image.open(f'static/upload/{filename}_{idx + 1}.jpg')
            content = pytesseract.image_to_string(img, lang='eng')

            Page(
                title=title,
                description=description,
                filename=filename,
                page_num=idx + 1,
                img_dir=img,
                content=content,
                writer=request.user,
            ).save()

        return redirect('uploader:uploader')
    else:
        uploadfileForm = UploadFileForm
        context = {
            'uploadfileForm': uploadfileForm,
        }
        return render(request, 'uploader/uploader.html', context)


# 각 페이지 별로 내용 ocr로 처리해서 문자로 변환함

# nlp로 유사어 처리해서 저장
# def nlp(request):
