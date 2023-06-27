# coding=utf-8

""" util-functions

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
import json


def extractDataFromJson(in_path: str) -> dict:
    out_data = {}

    with open(in_path, 'r') as file_reader:
        data = json.load(file_reader)

    for file_name, file_data in data.items():
        cnts = []

        for region in file_data['regions']:
            shape_attributes = region['shape_attributes']
            points_x = shape_attributes['all_points_x']
            points_y = shape_attributes['all_points_y']
            cnt = np.column_stack((points_x, points_y))
            cnts.append(cnt)

        out_data[file_data['filename']] = cnts

    return out_data


if __name__ == '__main__':
    import cv2 as cv

    _img_15 = cv.imread('../../data/fake(15).png')
    _img_16 = cv.imread('../../data/fake(16).png')

    _cnts_data = extractDataFromJson('../../data/test_mask.json')

    _img_15 = cv.drawContours(_img_15, _cnts_data['fake(15).png'], -1, (0, 0, 255), 3)
    _img_16 = cv.drawContours(_img_16, _cnts_data['fake(16).png'], -1, (0, 0, 255), 3)

    cv.imshow('_img_15', _img_15)
    cv.imshow('_img_16', _img_16)
    cv.waitKey()
