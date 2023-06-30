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

    __app = QApplication(sys.argv)
    __ui = QUiLoader().load("../../gui/main.ui", None)

    def __updateConfirmButtonState(self):
        if (self.__ui.images_label.text()[0] != '<') and (self.__ui.json_label.text()[0] != '<'):
            self.__ui.confirm_button.setEnabled(True)

    def __respondImagesButton(self):
        folder_path = QFileDialog.getExistingDirectory(None, "选择图片文件夹")

        if folder_path:
            self.__ui.images_label.setText(folder_path)
            self.__ui.images_button.setText("修改图片文件夹路径")
            self.__updateConfirmButtonState()

    def __resopondJsonButton(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "选择JSON文件", "", "JSON Files (*.json)")

        if file_path:
            self.__ui.json_label.setText(file_path)
            self.__ui.json_button.setText("修改JSON文件路径")
            self.__updateConfirmButtonState()

    def __respondConfirmButton(self):
        print('[INFO] button pressed.')
        images_path = self.__ui.images_label.text()
        json_path = self.__ui.json_label.text()
        print(f'[INFO] images_path: {images_path}')
        print(f'[INFO] json_path: {json_path}')
        self.__ui.confirm_button.setEnabled(False)

    # constructor and deconstructor

    def __init__(self):
        super().__init__()

        self.__ui.images_button.clicked.connect(self.__respondImagesButton)
        self.__ui.json_button.clicked.connect(self.__resopondJsonButton)
        self.__ui.confirm_button.clicked.connect(self.__respondConfirmButton)

        self.__ui.show()
        sys.exit(self.__app.exec())


if __name__ == '__main__':
    _ui = UserInterface()
