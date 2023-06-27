# coding=utf-8

""" Classes for converting JSON contours into PNG masks

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

import utils


class MaskConverter:
    """ Read JSON file and convert the contours into masks
    """

    def __init__(self, json_path:str):
        self.cnts_data = utils.extractDataFromJson(json_path)

    # public

    cnts_data = None

    def generateCanvas(self, in_path:str) -> np.ndarray:
        mask_height = 0
        mask_width = 0
        out_canvas = np.zeros([mask_height, mask_width], np.uint8)

        return out_canvas

    def drawAndFillContours(self, in_cnts:dict, in_mask:np.ndarray) -> np.ndarray:
        out_mask = in_mask.copy()

        return out_mask


if __name__ == '__main__':
    _json_path = '../../data/test_mask.json'
    _mask_converter = MaskConverter(_json_path)

    print(f'length of cnts_data: {len(_mask_converter.cnts_data)}')
