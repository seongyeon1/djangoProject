import json
import re
import pytesseract
import cv2

def tesseract_ocr_extract(image_path, sanction_list):
    image = cv2.imread(image_path)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pytesseract.image_to_data(rgb, output_type=pytesseract.Output.DICT)

    return_list = [{
            'x' : results["left"][i],
            'y' : results["top"][i],
            'w' : results["width"][i],
            'h' : results["height"][i],
            'color' : 'red',
            'text' : re.sub('[^a-zA-Z0-9]', '', results['text'][i]).strip(),
            'conf' : results["conf"][i]
            } for i in range(len(results["text"])) if (len(results['text'][i]) > 2) & (results['text'][i] in sanction_list)]

    return json.dumps(return_list)