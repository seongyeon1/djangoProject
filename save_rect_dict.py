import json
import cv2
from pytesseract import Output
import pytesseract
import re

# 사진에 박스를 치는 함수입니다.
# path : 파일경로
# sanction_list : 검출해야하는 대상을 리스트로 받습니다
def save_rect_dict(path, sanction_list):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # 테서렉트를 이용해 ocr 처리를 합니다
    d = pytesseract.image_to_data(image, output_type=Output.DICT)
    n_boxes = len(d['level'])
    boxes = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2RGB)
    rect = []
    cnt = 0

    for i in range(n_boxes):
        text = d['text'][i]
        text = re.sub('[^a-zA-Z0-9]', '', text).strip()

        if (text == '') & (len(text) < 3):
            continue

        sanction_list_all = ' '.join(sanction_list)
        sanction_list_all = re.sub('[^a-zA-Z0-9]', '', sanction_list_all).strip()

        if text in sanction_list_all:
            xmin = d['left'][i]
            ymin = d['top'][i]
            xmax = d['left'][i] + d['width'][i]
            ymax = d['top'][i] + d['height'][i]

            boxes = cv2.rectangle(boxes, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)

            rect.append({'boundingPoly': {'vertices': []}, 'uuid{}'.format(cnt): ''})
            rect[cnt]['boundingPoly']['vertices'].append(
                [{'x': ymin, 'y': xmin}, {'x': ymin, 'y': xmax}, {'x': ymax, 'y': xmax}, {'x': ymax, 'y': xmin}])

            rect[cnt]['uuid{}'.format(cnt)] = text
            cnt += 1

    return boxes