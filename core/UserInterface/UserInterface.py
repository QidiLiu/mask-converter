# coding=utf-8

""" Classes for user interface

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

import sys

from PySide6 import QtCore
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QFileDialog

class UserInterface(QtCore.QObject):

    # private

    __images_path = None
    __json_path = None
    __convert_func = None
    __app = QApplication(sys.argv)
    __ui = None

    def __updateConfirmButtonState(self):
        if (self.__ui.images_label.text()[0] != '<') and (self.__ui.json_label.text()[0] != '<'):
            self.__ui.confirm_button.setEnabled(True)

    def __respondImagesButton(self):
        folder_path_ = QFileDialog.getExistingDirectory(
            None,
            "選擇圖像所在資料夾 | Select folder path of images"
        )

        if folder_path_:
            self.__ui.images_label.setText(folder_path_)
            self.__ui.images_button.setText("修改圖像所在資料夾 | Change folder path of images")
            self.__updateConfirmButtonState()

    def __respondJsonButton(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "選擇JSON文件 | Select JSON file",
            "",
            "JSON Files (*.json)"
        )

        if file_path:
            self.__ui.json_label.setText(file_path)
            self.__ui.json_button.setText("修改JSON文件路徑 | Change JSON file")
            self.__updateConfirmButtonState()

    def __respondConfirmButton(self):
        self.__ui.confirm_button.setEnabled(False)
        self.__images_path = self.__ui.images_label.text()
        self.__json_path = self.__ui.json_label.text()
        self.__convert_func(self.__images_path, self.__json_path)

    # constructor and deconstructor

    def __init__(self, convert_func_, ui_path_:str):
        self.__convert_func = convert_func_
        super().__init__()
        self.__ui = QUiLoader().load(ui_path_, None)
        self.__ui.images_button.clicked.connect(self.__respondImagesButton)
        self.__ui.json_button.clicked.connect(self.__respondJsonButton)
        self.__ui.confirm_button.clicked.connect(self.__respondConfirmButton)

        self.__ui.show()
        sys.exit(self.__app.exec())


if __name__ == '__main__':
    sys.path.append('../MaskConverter')
    import MaskConverter

    ui = UserInterface(MaskConverter.convert, "../../gui/main.ui")
