import json
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pytesseract import Output
import pytesseract
import re

# def plot_rgb(image):
#     plt.figure(figsize=(30, 15))
#     return plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

def save_rect_dict(path, sanction_list):
    rect = []
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
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

        sanction_list_all = ''.join(sanction_list)

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

    #plot_rgb(boxes)

    return boxes