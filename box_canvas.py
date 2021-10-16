import json
import re
import pytesseract
import cv2

# TESSERACT를 이용해서 JSON으로 SANCTION LIST에 있는 데이터를 뽑아내는 함수입니다
def tesseract_ocr_extract(image_path, box):
    image = cv2.imread(image_path)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pytesseract.image_to_data(rgb, output_type=pytesseract.Output.DICT)

    # SANCTION LIST를 하나로 묶었습니다
    sanction_all = ' '.join(box.keys())

    return_list = [{
            'x' : results["left"][i],
            'y' : results["top"][i],
            'w' : results["width"][i],
            'h' : results["height"][i],
            'color' : 'red',
            'text' : re.sub('[^a-zA-Z0-9]', '', results["text"][i]).strip(),
            'conf' : results["conf"][i]
            } for i in range(len(results["text"])) if (len(results["text"][i]) > 2) & (results["text"][i] in sanction_all)]

    return json.dumps(return_list)