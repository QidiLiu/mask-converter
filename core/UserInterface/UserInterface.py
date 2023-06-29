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
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

class UserInterface(QtCore.QObject):

    # public

    app = QApplication(sys.argv)
    ui = QUiLoader().load("../../gui/main.ui", None)

    def respondConfirmButton(self):
        print('[INFO] button pressed.')

    # constructor and deconstructor

    def __init__(self):
        super().__init__()

        self.ui.setWindowTitle("Mask Converter")
        self.ui.confirm_button.clicked.connect(self.respondConfirmButton)

        self.ui.show()
        sys.exit(self.app.exec())


if __name__ == '__main__':
    _ui = UserInterface()

