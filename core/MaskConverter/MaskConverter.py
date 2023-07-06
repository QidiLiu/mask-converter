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

def extractDataFromJson(in_path:str) -> dict:
    out_data_ = {}

    with open(in_path, 'r') as file_reader_:
        data_ = json.load(file_reader_)

    for _, file_data in data_.items():
        cnts_ = []

        for region in file_data['regions']:
            shape_attributes_ = region['shape_attributes']
            points_x_ = shape_attributes_['all_points_x']
            points_y_ = shape_attributes_['all_points_y']
            cnt_ = np.column_stack((points_x_, points_y_))
            cnts_.append(cnt_)

        out_data_[file_data['filename']] = cnts_

    return out_data_

def convert(images_path: str, json_path: str):
    cnts_data_ = extractDataFromJson(json_path)
    img_paths_ = glob(images_path + '/*.png')

    for img_path in img_paths_:
        img_path = img_path.replace('\\', '/')
        img_ = cv.imread(img_path)
        img_file_name_ = img_path.split('/')[-1]
        canvas_ = np.zeros(img_.shape, np.uint8)
        mask_ = cv.drawContours(canvas_, cnts_data_[img_file_name_], -1, (255, 255, 255), cv.FILLED)
        cv.imwrite(img_path.replace('.png', '_mask.png'), mask_)

    print('[INFO] Conversion finished.')


if __name__ == '__main__':
    _img_15 = cv.imread('../../data/fake(15).png')
    _img_16 = cv.imread('../../data/fake(16).png')

    _cnts_data = extractDataFromJson('../../data/test_mask.json')

    _img_15 = cv.drawContours(_img_15, _cnts_data['fake(15).png'], -1, (0, 0, 255), 3)
    _img_16 = cv.drawContours(_img_16, _cnts_data['fake(16).png'], -1, (0, 0, 255), 3)

    cv.imshow('_img_15', _img_15)
    cv.imshow('_img_16', _img_16)
    cv.waitKey()
