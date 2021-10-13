import glob, os, cv2

from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

## Python이 실행될 때 DJANGO_SETTINGS_MODULE이라는 환경 변수에 현재 프로젝트의 settings.py파일 경로를 등록합니다.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")

## 이제 장고를 가져와 장고 프로젝트를 사용할 수 있도록 환경을 만듭니다.
import django
django.setup()

# 저장할 모델 가져오기
from mysite.models import Page

# 테서렉트 준비
import pytesseract
try:
    from PIL import Image
except:
    import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'my_app'
    verbose_name = "My App"

    @csrf_exempt
    def file_to_text():
        files = [os.path.basename(x) for x in glob.glob('./docs/upload/**/*.tif', recursive=True)]
        for infile in files:
            filename = infile[:-4]
            print("file : " + filename)
            ret, images = cv2.imreadmulti('./docs/upload/' + infile, [], cv2.IMREAD_ANYCOLOR)

            for idx, img in enumerate(images):
                # 페이지 이미지 저장하기
                cv2.imwrite(f'static/img/{filename}_{idx + 1}.jpg', img)
                # 페이지 이미지 열기
                img = Image.open(f'static/img/{filename}_{idx + 1}.jpg')
                content = pytesseract.image_to_string(img, lang='eng')

                Page(
                    filename=filename,
                    page_num=idx+1,
                    img_dir=img,
                    content=content,
                ).save()