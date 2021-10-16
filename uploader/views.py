import cv2
import os, re

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

import jellyfish
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
            # 테서렉트를 이용해서 이미지에서 글자 추출
            content = pytesseract.image_to_string(img, lang='eng')

            # 글자와 비교할 제재 목록 가져오기
            sanction_list = SanctionMain.objects.all().values_list('sdn_name', flat=True)

            # 사진에 바로 BOX 쳐서 저장하고 싶은경우 -> SANCTION LIST에 들어가 있는 TEXT 박스쳐서 저장
            # box = save_rect_dict(f'static/upload/{filename}_{idx + 1}.jpg', sanction_list)
            # cv2.imwrite(f'static/upload/{filename}_{idx + 1}.box.jpg', box)

            # box list
            box = {}
            sdn_name = {}
            # full matching
            for sanction in sanction_list:
                if sanction in content:
                    sdn_name[sanction] = 100
                    box[sanction] = 100

            docs = []
            for s in content.split():
                s = re.sub(r"[^a-zA-Z0-9 ]", "", s)
                if len(s) > 2:
                    docs.append(s)

            # 임계치 데이터를 가져옴
            r = threshold[0].threshold
            for doc in docs:
                for sanction in sanction_list:
                    sanction = re.sub(r"[^a-zA-Z0-9 ]", "", sanction)
                    if jellyfish.jaro_winkler(sanction, doc) * 100 > r:
                        score = round(jellyfish.jaro_winkler(sanction, doc) * 100, 0)
                        sdn_name[sanction] = score
                        box[doc] = score

            result = box
            json_list = tesseract_ocr_extract(f'static/upload/{filename}_{idx + 1}.jpg', result)
            f = File.objects.get(filename=filename)
            Page(
                file=f,
                title=title,
                description=description,
                filename=filename,
                page_num=idx + 1,
                box_json=json_list,
                content=result,
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