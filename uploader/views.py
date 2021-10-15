import cv2
import os

import pytesseract  # ======= > Add
import simplejson
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from mysite.models import File, Page
from sanction.models import SanctionMain
from threshold.models import SetThreshold
from .forms import UploadFileForm

try:
    from PIL import Image
except:
    import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from save_rect_dict import save_rect_dict
from box_canvas import tesseract_ocr_extract

# 파일 업로드 (tif 확장자만 허용)
@login_required
@csrf_exempt
def uploadfile(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        file = request.FILES['file']

        # uploadfile = UploadFile(
        #     title=title,
        #     description=description,
        #     file=file,
        #     writer=request.user,
        # )
        # uploadfile.save()

        file_dir = file.temporary_file_path()
        filename = os.path.basename(file_dir).split('.')[0]

        threshold = SetThreshold.objects.raw('SELECT * FROM threshold_setthreshold ORDER BY set_date DESC LIMIT 1')
        upload = File(
            title=title,
            file=file,
            filename=filename,
            threshold=threshold[0],
            description=description,
            writer=request.user,
        )
        upload.save()

        ret, images = cv2.imreadmulti(file_dir, [], cv2.IMREAD_ANYCOLOR)

        for idx, img in enumerate(images):
            # 페이지 이미지 저장하기
            cv2.imwrite(f'static/upload/{filename}_{idx + 1}.jpg', img)
            # 페이지 이미지 열기
            img = Image.open(f'static/upload/{filename}_{idx + 1}.jpg')
            content = pytesseract.image_to_string(img, lang='eng')
            sanction_list = SanctionMain.objects.all().values_list('sdn_name', flat=True)

            box = save_rect_dict(f'static/upload/{filename}_{idx + 1}.jpg', sanction_list)
            cv2.imwrite(f'static/upload/{filename}_{idx + 1}.box.jpg', box)

            json_list = tesseract_ocr_extract(f'static/upload/{filename}_{idx + 1}.jpg', sanction_list)
            f = File.objects.get(filename=filename)
            Page(
                file=f,
                title=title,
                description=description,
                filename=filename,
                page_num=idx + 1,
                box_json=json_list,
                content=content,
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
