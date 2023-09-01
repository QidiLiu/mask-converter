# coding=utf-8

""" Functions for converting JSON contours into PNG masks

License notice:
   Copyright 2023 劉啟迪(QidiLiu)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

__author__ = 'QidiLiu'

import numpy as np
import cv2 as cv
import json
from glob import glob

def extractDataFromJson(in_path_:str) -> dict:
    out_data = {}

    with open(in_path_, 'r') as file_reader:
        data = json.load(file_reader)

    for _, file_data in data.items():
        cnts = []

        for region in file_data['regions']:
            shape_attributes = region['shape_attributes']
            points_x = shape_attributes['all_points_x']
            points_y = shape_attributes['all_points_y']
            cnt = np.column_stack((points_x, points_y))
            cnts.append(cnt)

        out_data[file_data['filename']] = cnts

    return out_data

def convert(img_paths_: str, json_path_: str):
    cnts_data = extractDataFromJson(json_path_)
    img_paths = glob(img_paths_ + '/*.png')

    for img_path in img_paths:
        img_path = img_path.replace('\\', '/')
        img = cv.imread(img_path)
        img_file_name = img_path.split('/')[-1]
        canvas = np.zeros(img.shape, np.uint8)
        mask = cv.drawContours(canvas, cnts_data[img_file_name], -1, (255, 255, 255), cv.FILLED)
        cv.imwrite(img_path.replace('.png', '_mask.png'), mask)

    print('[INFO] Conversion finished.')


if __name__ == '__main__':
    img_15 = cv.imread('../../data/fake(15).png')
    img_16 = cv.imread('../../data/fake(16).png')

    cnts_data = extractDataFromJson('../../data/test_mask.json')

    img_15 = cv.drawContours(img_15, cnts_data['fake(15).png'], -1, (0, 0, 255), 3)
    img_16 = cv.drawContours(img_16, cnts_data['fake(16).png'], -1, (0, 0, 255), 3)

    cv.imshow('_img_15', img_15)
    cv.imshow('_img_16', img_16)
    cv.waitKey()
