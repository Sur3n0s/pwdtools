import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import Qt, QtCore

# version: pwdtools 1.1

class DialogMain(QDialog):
    def __init__(self):
        super().__init__()

        # Main Window

        self.setWindowTitle("Password Tools")
        self.setFixedHeight(490)
        self.setFixedWidth(760)
        self.setStyleSheet("background-color: '#000918';")
        self.AllComponents()
        self.ceasar()

    def AllComponents(self):

        # Frames

        self.frameFirst = QFrame(self)
        self.frameFirst.setGeometry(20, 20, 720, 90)
        self.frameFirst.setStyleSheet("background-color: '#00173c';" +
                                      "border: none;")

        self.frameSecond = QFrame(self)
        self.frameSecond.setGeometry(20, 130, 720, 150)
        self.frameSecond.setStyleSheet("background-color: '#00173c';" +
                                       "border: none;")

        self.frameThird = QFrame(self)
        self.frameThird.setGeometry(20, 300, 720, 170)
        self.frameThird.setStyleSheet("background-color: '#00173c';" +
            "border: none;")

        self.frameBlueLine = QFrame(self)
        self.frameBlueLine.setGeometry(20, 101, 720, 10)
        self.frameBlueLine.setStyleSheet("QFrame {"
            "background-color: '#00098e';" +
            "border: none;"
            "}")

        self.frameGreyDecorationLine = QFrame(self)
        self.frameGreyDecorationLine.setGeometry(40, 170, 681, 1)
        self.frameGreyDecorationLine.setStyleSheet("background-color: '#d8d8d8';")

        # LineEdit

        self.lineEditPassword = QLineEdit("Password", self)
        self.lineEditPassword.setGeometry(50, 40, 520, 40)
        self.lineEditPassword.setReadOnly(True)
        self.lineEditPassword.setCursor(QtCore.Qt.IBeamCursor)
        self.lineEditPassword.setStyleSheet(" QLineEdit {"
            "background: '#00173c';" +
            "color: '#d8d8d8';" +
            "border: none;" +
            "font-size: 30px;" +
            "font-family: monospace;" +
            "}")

        # Labels

        self.labelPasswwordLenght = QLabel("Password Lenght", self)
        self.labelPasswwordLenght.setFont(Qt.QFont("Monospace", 10))
        self.labelPasswwordLenght.setGeometry(40, 180, 130, 20)
        self.labelPasswwordLenght.setStyleSheet("QLabel {"
            "color: '#d8d8d8';" +
            "background-color: none;" +
            "}")

        self.labelCustomize = QLabel("Customize your password", self)
        self.labelCustomize.setFont(Qt.QFont("Monospace", 15))
        self.labelCustomize.setGeometry(40, 130, 350, 40)
        self.labelCustomize.setStyleSheet("QLabel {"
            "color: '#d8d8d8';" +
            "background-color: none;" +
            "}")

        # Buttons

        self.buttonGenerate = QPushButton(self)
        self.buttonGenerate.setGeometry(660, 30, 64, 64)
        self.buttonGenerate.setToolTip('<p style="color:black;">Refresh</p>')
        self.buttonGenerate.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonGenerate.clicked.connect(self.password_generation)
        self.buttonGenerate.setStyleSheet("QPushButton {"
            "background-image: url(img/refresh_white.png);" +
            "border-radius: 30px;" +
            "background-color: none;" +
            "border: none;"
            "}"

            "QPushButton:hover {"
            "background-color: '#2b2b91';"
            "}"

            "QPushButton:pressed {"
            "background-color: '#2f2fce';"
            "}")

        self.buttonCopy = QPushButton(self)
        self.buttonCopy.setGeometry(590, 30, 64, 64)
        self.buttonCopy.setToolTip('<p style="color: black;">Copy</p>')
        self.buttonCopy.setCursor(QtCore.Qt.PointingHandCursor)
        self.buttonCopy.clicked.connect(self.button_copy)
        self.buttonCopy.setStyleSheet("QPushButton {"
            "background-image: url(img/copy_white.png);" +
            "border-radius: 5px;" +
            "background-color: none;" +
            "border: none;" +
            "}"

            "QPushButton:hover {"
            "background-color: '#2b2b91';"
            "}"

            "QPushButton:pressed {"
            "background-color: '#2f2fce';" +
            "}")

        # RadioButtons

        self.radioButtonEasySay = QRadioButton("Easy to say", self)
        self.radioButtonEasySay.setFont(Qt.QFont("Monospace", 10))
        self.radioButtonEasySay.setGeometry(350, 180, 190, 22)
        self.radioButtonEasySay.toggled.connect(self.radio_buttons_options)
        self.radioButtonEasySay.setStyleSheet("QRadioButton {"
            "background-color: none;" +
            "color: '#d8d8d8';"
            "}"

            "QRadioButton::indicator:checked {" +
            "width: 16px;" +
            "height: 16px;" +
            "background-image: url(img/radio_button_white.png);" +
            "}" +

            "QRadioButton::indicator:unchecked {" +
            "width: 16px;" +
            "height: 16px;" +
            "background-image: url(img/radio_button_white_unchecked.png);"
            "}")

        self.radioButtonEasyRead = QRadioButton("Easy to read", self)
        self.radioButtonEasyRead.setFont(Qt.QFont("Monospace", 10))
        self.radioButtonEasyRead.setGeometry(350, 210, 190, 22)
        self.radioButtonEasyRead.toggled.connect(self.radio_buttons_options)
        self.radioButtonEasyRead.setStyleSheet("QRadioButton {"
            "background-color: none;" +
            "color: '#d8d8d8';" +
            "}"

            "QRadioButton::indicator:checked {" +
            "width: 16px;" +
            "height: 16px;" +
            "background-image: url(img/radio_button_white.png);" +
            "}" +

            "QRadioButton::indicator:unchecked {" +
            "width: 16px;" +
            "height: 16px;" +
            "background-image: url(img/radio_button_white_unchecked.png);"
            "}")

        self.radioButtonAllChar = QRadioButton("All Characters", self)
        self.radioButtonAllChar.setFont(Qt.QFont("Monospace", 10))
        self.radioButtonAllChar.setGeometry(350, 240, 190, 22)
        self.radioButtonAllChar.setChecked(True)
        self.radioButtonAllChar.toggled.connect(self.radio_buttons_options)
        self.radioButtonAllChar.setStyleSheet("QRadioButton {"
            "background-color: none;" +
            "color: '#d8d8d8';"
            "}"

            "QRadioButton::indicator:checked {" +
            "width: 16px;" +
            "height: 16px;" +
            "background-image: url(img/radio_button_white.png);" +
            "}" +

            "QRadioButton::indicator:unchecked {" +
            "width: 16px;" +
            "height: 16px;" +
            "background-image: url(img/radio_button_white_unchecked.png);"
            "}")

        # CheckBoxes

        self.checkBoxUppercase = QCheckBox("Uppercase", self)
        self.checkBoxUppercase.setFont(Qt.QFont("Monospace", 10))
        self.checkBoxUppercase.setGeometry(550, 180, 170, 22)
        self.checkBoxUppercase.setChecked(True)
        self.checkBoxUppercase.setStyleSheet("QCheckBox {"
            "color: '#d8d8d8';" +
            "background-color: none;" +
            "}" +

            "QCheckBox::indicator:hover {"
            "background-color: '#2b2b91';"
            "}"

            "QCheckBox::indicator:unchecked {" +
            "background-image: url(img/checkbox_unchecked_white.png);" +
            "}" +

            "QCheckBox::indicator {" +
            "width: 16px;" +
            "height: 16px;" +
            "background-color: none;" +
            "background-image: url(img/checkbox_white.png);" +
            "}")


        self.checkBoxLowercase = QCheckBox("Lowercase", self)
        self.checkBoxLowercase.setFont(Qt.QFont("Monospace", 10))
        self.checkBoxLowercase.setGeometry(550, 200, 170, 22)
        self.checkBoxLowercase.setChecked(True)
        self.checkBoxLowercase.setStyleSheet("QCheckBox {"
            "color: '#d8d8d8';" +
            "background-color: none;" +
            "}" +

            "QCheckBox::indicator:hover {"
            "background-color: '#2b2b91';"
            "}"

            "QCheckBox::indicator:unchecked {" +
            "background-image: url(img/checkbox_unchecked_white.png);" +
            "}" +

            "QCheckBox::indicator {" +
            "width: 16px;" +
            "height: 16px;" +
            "background-color: none;" +
            "background-image: url(img/checkbox_white.png);" +
            "}")

        self.checkBoxNumbers = QCheckBox("Numbers", self)
        self.checkBoxNumbers.setFont(Qt.QFont("Monospace", 10))
        self.checkBoxNumbers.setGeometry(550, 220, 170, 22)
        self.checkBoxNumbers.setStyleSheet("QCheckBox {"
            "color: '#d8d8d8';" +
            "background-color: none;" +
            "}" +

            "QCheckBox::indicator:hover {"
            "background-color: '#2b2b91';"
            "}"

            "QCheckBox::indicator:unchecked {" +
            "background-image: url(img/checkbox_unchecked_white.png);" +
            "}" +

            "QCheckBox::indicator {" +
            "width: 16px;" +
            "height: 16px;" +
            "background-color: none;" +
            "background-image: url(img/checkbox_white.png);" +
            "}")

        self.checkBoxSymbols = QCheckBox("Symbols", self)
        self.checkBoxSymbols.setFont(Qt.QFont("Monospace", 10))
        self.checkBoxSymbols.setGeometry(550, 240, 170, 22)
        self.checkBoxSymbols.setStyleSheet("QCheckBox {"
            "color: '#d8d8d8';" +
            "background-color: none;" +
            "}" +

            "QCheckBox::indicator:hover {"
            "background-color: '#2b2b91';"
            "}"

            "QCheckBox::indicator:unchecked {" +
            "background-image: url(img/checkbox_unchecked_white.png);" +
            "}" +

            "QCheckBox::indicator {" +
            "width: 16px;" +
            "height: 16px;" +
            "background-color: none;" +
            "background-image: url(img/checkbox_white.png);" +
            "}")

        # Slider

        self.SliderValue = QSlider(self,
                              value=10,
                              maximum=50,
                              minimum=1)
        self.SliderValue.setGeometry(100, 225, 160, 20)
        self.SliderValue.setOrientation(QtCore.Qt.Horizontal)
        self.SliderValue.setToolTip(str(self.SliderValue.value()))
        self.SliderValue.valueChanged.connect(self.slider_value_synchronization)
        self.SliderValue.setStyleSheet("QSlider {"
            "background-color: none;"
            "}"

            "QSlider::groove:horizontal {" +
            "border: 1px solid grey;" +
            "border-radius: 2px;"
            "background: black;" +
            "height: 5px;" +
            "}"

            "QSlider::handle:horizontal {"
            "background-color: none;" +
            "width: 16px;" +
            "margin-top: -6px;" +
            "margin-bottom: -4px;" +
            "background-image: url(img/ratio_white.png);" +
            "}")

        # Spinbox

        self.spinBoxValue = QSpinBox(self,
                                value=10,
                                maximum=50,
                                minimum=1,
                                singleStep=1)
        self.spinBoxValue.setGeometry(40, 220, 52, 32)
        self.spinBoxValue.valueChanged.connect(self.spinbox_value_synchronization)
        self.spinBoxValue.setStyleSheet("QSpinBox {"
            "color: '#d8d8d8';" +
            "border: 2px solid '#d8d8d8';" +
            "border-radius: 5px;" +
            "font-size: 15px;" +
            "background-color: '#00173c';" +
            "padding-left: 5px;" +
            "}"

            "QSpinBox::down-button {" +
            "width: 16px;" +
            "background-color: none;" +
            "border: 0px solid" +
            "}"
            
            "QSpinBox::down-button:hover {" +
            "border-radius: 2px;" +
            "background-color: '#2b2b91';" +
            "}"

            "QSpinBox::down-button:pressed {" +
            "background-color: '#2f2fce';" +
            "}"

            "QSpinBox::down-arrow {" +
            "background-image: url(img/down_arrow_white8x8.png);" +
            "height: 8px;" +
            "width: 8px;" +
            "margin-top: 4px;" +
            "margin-bottom: 2px;"
            "}"

            "QSpinBox::up-button {" +
            "width: 16px;" +
            "background-color: none;" +
            "border: 0px solid" +
            "}"
            
            "QSpinBox::up-button:hover {" +
            "border-radius: 2px;" +
            "background-color: '#2b2b91';" +
            "}"

            "QSpinBox::up-button:pressed {" +
            "background-color: '#2f2fce';" +
            "}"

            "QSpinBox::up-arrow {" +
            "background-image: url(img/up_arrow_white8x8.png);" +
            "height: 8px;" +
            "width: 8px;" +
            "margin-top: 4px;" +
            "margin-bottom: 2px;"
            "}")

    #Functions

    def slider_value_synchronization(self):
        current = self.SliderValue.value()
        self.spinBoxValue.setValue(current)
        self.password_generation()

    def spinbox_value_synchronization(self):
        current = self.spinBoxValue.value()
        self.SliderValue.setValue(current)
        self.password_generation()

    def password_generation(self):

        # Lists

        list_uppcase = ('QWERTYUIOPASDFGHJKLZXCVBNM')
        list_lowcase = ('qwertyuiopasdfghjklzxcvbnm')
        list_numbers = ('1234567890')
        list_symbols = ('!@#$%^&*()_=+-<>?/\\|~')
        list_main = ''

        cBUppercase = self.checkBoxUppercase.isChecked()
        cBLowercase = self.checkBoxLowercase.isChecked()
        cBNumbers = self.checkBoxNumbers.isChecked()
        cBSymbols = self.checkBoxSymbols.isChecked()

        # Operations

        if not False in {cBUppercase, cBLowercase, cBNumbers, cBSymbols}:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase +
                    list_lowcase + list_numbers + list_symbols)
                self.lineEditPassword.setText(list_main)

        elif not False in {cBUppercase, cBLowercase, cBNumbers}:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase +
                    list_lowcase + list_numbers)
                self.lineEditPassword.setText(list_main)

        elif not False in {cBUppercase, cBLowercase, cBSymbols}:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase +
                    list_lowcase + list_symbols)
                self.lineEditPassword.setText(list_main)

        elif not False in {cBUppercase, cBNumbers, cBSymbols}:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase +
                    list_numbers + list_symbols)
                self.lineEditPassword.setText(list_main)

        elif not False in {cBLowercase, cBNumbers, cBSymbols}:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_lowcase +
                    list_numbers + list_symbols)
                self.lineEditPassword.setText(list_main)

        elif not False in {cBUppercase, cBLowercase}:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase +
                    list_lowcase)
                self.lineEditPassword.setText(list_main)

        elif not False in {cBLowercase, cBNumbers}:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_lowcase +
                    list_numbers)
                self.lineEditPassword.setText(list_main)

        elif not False in {cBNumbers, cBSymbols}:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_numbers +
                    list_symbols)
                self.lineEditPassword.setText(list_main)

        elif not False in {cBUppercase, cBNumbers}:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase +
                    list_numbers)
                self.lineEditPassword.setText(list_main)

        elif not False in {cBLowercase, cBSymbols}:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_lowcase +
                    list_symbols)
                self.lineEditPassword.setText(list_main)

        elif not False in {cBUppercase, cBSymbols}:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase +
                    list_symbols)
                self.lineEditPassword.setText(list_main)

        elif not False in {cBSymbols}:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_symbols)
                self.lineEditPassword.setText(list_main)

        elif not False in {cBNumbers}:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_numbers)
                self.lineEditPassword.setText(list_main)

        elif not False in {cBUppercase}:
            for x in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase)
                self.lineEditPassword.setText(list_main)

        elif not False in {cBLowercase}:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_lowcase)
                self.lineEditPassword.setText(list_main)

        else:
            self.lineEditPassword.setText('*Empty*')

    def radio_buttons_options(self):
        if self.radioButtonEasyRead.isChecked():
            self.checkBoxSymbols.setEnabled(False)
            self.checkBoxNumbers.setEnabled(False)
            self.checkBoxSymbols.setChecked(False)
            self.checkBoxNumbers.setChecked(False)
            self.checkBoxSymbols.setStyleSheet("QCheckBox::indicator {" +
                "width: 16px;" +
                "height: 16px;" +
                "background-color: none;" +
                "background-image: url(img/checkbox_deactivated.png);" +
                "}"

                "QCheckBox {" +
                "background-color: none;" +
                "}")

            self.checkBoxNumbers.setStyleSheet("QCheckBox::indicator {" +
                "width: 16px;" +
                "height: 16px;" +
                "background-color: none;" +
                "background-image: url(img/checkbox_deactivated.png);" +
                "}"

                "QCheckBox {" +
                "background-color: none;" +
                "}")

        elif self.radioButtonEasySay.isChecked():
            self.checkBoxSymbols.setEnabled(False)
            self.checkBoxNumbers.setEnabled(False)
            self.checkBoxSymbols.setChecked(False)
            self.checkBoxNumbers.setChecked(False)
            self.checkBoxSymbols.setStyleSheet("QCheckBox::indicator {" +
                "width: 16px;" +
                "height: 16px;" +
                "background-color: none;" +
                "background-image: url(img/checkbox_deactivated.png);" +
                "}"

                "QCheckBox {" +
                "background-color: none;" +
                "}")

            self.checkBoxNumbers.setStyleSheet("QCheckBox::indicator {" +
                "width: 16px;" +
                "height: 16px;" +
                "background-color: none;" +
                "background-image: url(img/checkbox_deactivated.png);" +
                "}"

                "QCheckBox {" +
                "background-color: none;" +
                "}")

        else:
            self.checkBoxSymbols.setEnabled(True)
            self.checkBoxNumbers.setEnabled(True)
            self.checkBoxSymbols.setStyleSheet("QCheckBox {"
                "color: '#d8d8d8';" +
                "background-color: none;" +
                "}" +

                "QCheckBox::indicator:hover {"
                "background-color: '#2b2b91';"
                "}"

                "QCheckBox::indicator:unchecked {" +
                "background-image: url(img/checkbox_unchecked_white.png);" +
                "}" +

                "QCheckBox::indicator {" +
                "width: 16px;" +
                "height: 16px;" +
                "background-color: none;" +
                "background-image: url(img/checkbox_white.png);" +
                "}")

            self.checkBoxNumbers.setStyleSheet("QCheckBox {"
                "color: '#d8d8d8';" +
                "background-color: none;" +
                "}" +

                "QCheckBox::indicator:hover {"
                "background-color: '#2b2b91';"
                "}"

                "QCheckBox::indicator:unchecked {" +
                "background-image: url(img/checkbox_unchecked_white.png);" +
                "}" +

                "QCheckBox::indicator {" +
                "width: 16px;" +
                "height: 16px;" +
                "background-color: none;" +
                "background-image: url(img/checkbox_white.png);" +
                "}")

    def button_copy(self):
        copy = QApplication.clipboard()
        copy.clear(mode=copy.Clipboard)
        copy.setText(self.lineEditPassword.text(), mode=copy.Clipboard)

    #########################
    ######CEASAR CIPHER######
    #########################

    def ceasar(self):

        operations = ["Encrypt", "Decrypt"]
        offset = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]

        # Result Label

        self.ceasarResult = QLineEdit(self)
        self.ceasarResult.setGeometry(40, 350, 627, 30)
        self.ceasarResult.setReadOnly(True)
        self.ceasarResult.setFont(Qt.QFont("Monospace", 10))
        self.ceasarResult.setAlignment(QtCore.Qt.AlignCenter)
        self.ceasarResult.setCursor(QtCore.Qt.IBeamCursor)
        self.ceasarResult.setPlaceholderText("Your message will be here")
        self.ceasarResult.setStyleSheet("background-color: '#d8d8d8';"
            "border: 2px solid black;" +
            "border-top-left-radius: 15px;" +
            "border-bottom-left-radius: 15px;" +
            "text-align: center;")

        # LineEdit

        self.ceasarLineEdit = QLineEdit("", self)
        self.ceasarLineEdit.setGeometry(40, 390, 627, 30)
        self.ceasarLineEdit.setFont(Qt.QFont("Monospace", 10))
        self.ceasarLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ceasarLineEdit.setMaxLength(100)
        self.ceasarLineEdit.setPlaceholderText("Type here something...")
        self.ceasarLineEdit.setStyleSheet("border: 2px solid black;" +
            "border-top-left-radius: 15px;" +
            "border-bottom-left-radius: 15px;" +
            "background-color: '#d8d8d8';")

        # ComboBoxes

        self.ceasarComboBoxOperations = QComboBox(self)
        #self.ceasarComboBoxOperations.setFont(Qt.QFont("Monospace", 9))
        self.ceasarComboBoxOperations.setGeometry(120, 432, 120, 20)
        self.ceasarComboBoxOperations.addItems(operations)
        self.ceasarComboBoxOperations.setStyleSheet("QComboBox {"
            "background-color: '#d8d8d8';" +
            "border: 0px solid;" +
            "border-radius: 5px;" +
            "}"

            "QComboBox::drop-down {"
            "background-color: none;" +
            "border-radius: 4px;" +
            "}"

            "QComboBox::drop-down:hover {"
            "background-color: grey;" +
            "}"

            "QComboBox::down-arrow {" +
            "width: 12px;" +
            "background-image: url(img/down_arrow_test10x10.png);" +
            "margin-top: 2px;" +
            "padding-right: -2px;" +
            "}" +

            "QComboBox QListView {" +
            "background-color: '#d8d8d8';" +
            "}")

        self.ceasarComboBoxOffset = QComboBox(self)
        #self.ceasarComboBoxOffset.setFont(Qt.QFont("Monospace", 9))
        self.ceasarComboBoxOffset.setGeometry(310, 432, 50, 20)
        self.ceasarComboBoxOffset.addItems(offset)
        self.ceasarComboBoxOffset.setStyleSheet("QComboBox {"
            "background-color: '#d8d8d8';" +
            "border: 0px solid;" +
            "border-radius: 5px;" +
            "}"

            "QComboBox::drop-down {"
            "background-color: none;" +
            "border-radius: 4px;" +
            "}"

            "QComboBox::drop-down:hover {"
            "background-color: grey;" +
            "}"

            "QComboBox QScrollBar::vertical {"
            "background-color: '#2255a5';"
            "width: 15px;"
            "border: 0px solid;"
            "border-radius: 4px;"
            "}"

            "QComboBox QScrollBar::handle:vertical {"
            "width: 15px;"
            "background: '#00173c';"
            "border: 0px solid;"
            "border-radius: 7px;"
            "}"

            "QComboBox::down-arrow {" +
            "width: 12px;" +
            "background-image: url(img/down_arrow_test10x10.png);" +
            "margin-top: 2px;" +
            "padding-right: -2px;" +
            "}" +

            "QComboBox QListView {" +
            "background-color: '#d8d8d8';" +
            "}")

        # Labels

        self.ceasarLabelSign = QLabel("Ceasar Cipher", self)
        self.ceasarLabelSign.setFont(Qt.QFont("Monospace", 15))
        self.ceasarLabelSign.setGeometry(40, 300, 300, 40)
        self.ceasarLabelSign.setStyleSheet("QLabel {"
            "color: '#d8d8d8';" +
            "background-color: none;"
            "}")

        self.ceasarLabelOperaiton = QLabel("Operation:", self)
        self.ceasarLabelOperaiton.setGeometry(40, 432, 80, 20)
        self.ceasarLabelOperaiton.setFont(Qt.QFont("Monospace", 10))
        self.ceasarLabelOperaiton.setStyleSheet("QLabel {"
            "background-color: none;" +
            "color: '#d8d8d8';" +
            "}")

        self.ceasarLabelOffset = QLabel("Offset:", self)
        self.ceasarLabelOffset.setFont(Qt.QFont("Monospace", 10))
        self.ceasarLabelOffset.setGeometry(250, 432, 60, 20)
        self.ceasarLabelOffset.setStyleSheet("QLabel {"
            "background-color: none;" +
            "color: '#d8d8d8'"
            "}")

        # Buttons

        self.ceasarButtonEncrypt = QPushButton("Encrypt/Decrypt", self)
        self.ceasarButtonEncrypt.setFont(Qt.QFont("Monospace", 8))
        self.ceasarButtonEncrypt.setGeometry(380, 430, 340, 25)
        self.ceasarButtonEncrypt.setCursor(QtCore.Qt.PointingHandCursor)
        self.ceasarButtonEncrypt.clicked.connect(self.ceasar_encrypt_decrypt_button)
        self.ceasarButtonEncrypt.setStyleSheet("QPushButton {"
            "border: 2px solid black;" +
            "border-radius: 10px;" +
            "background-color: '#d8d8d8';"
            "}"

            "QPushButton::hover {" +
            "background-color: '#5fb25c';" +
            "border: 3px solid black;" +
            "}"

            "QPushButton::pressed {" +
            "background-color: '#24a320'" +
            "}")

        self.ceasarButtonCopyResult = QPushButton("Copy", self)
        self.ceasarButtonCopyResult.setFont(Qt.QFont("Monospace", 9))
        self.ceasarButtonCopyResult.setGeometry(665, 350, 35, 30)
        self.ceasarButtonCopyResult.setCursor(QtCore.Qt.PointingHandCursor)
        self.ceasarButtonCopyResult.clicked.connect(self.ceasar_copy_result)
        self.ceasarButtonCopyResult.setStyleSheet("QPushButton {"
            "background-color: '#d8d8d8';" +
            "border: 2px solid black;" +
            "border-bottom-right-radius: 15px;" +
            "border-top-right-radius: 15px;"
            "}"

            "QPushButton::hover {" +
            "background-color: '#5c75b2';" +
            "border: 2px solid black;" +
            "}"

            "QPushButton::pressed {" +
            "background-color: '#3156b2';" +
            "}")

        self.ceasarButtonCleanResult = QPushButton("Clean", self)
        self.ceasarButtonCleanResult.setFont(Qt.QFont("Monospace", 9))
        self.ceasarButtonCleanResult.setGeometry(622, 350, 45, 30)
        self.ceasarButtonCleanResult.setCursor(QtCore.Qt.PointingHandCursor)
        self.ceasarButtonCleanResult.clicked.connect(self.ceasar_clean_result)
        self.ceasarButtonCleanResult.setStyleSheet("QPushButton {"
            "background-color: '#d8d8d8';" +
            "border: 2px solid black;" +
            "}"

            "QPushButton::hover {" +
            "background-color: '#b25c5e';" +
            "border: 2px solid black;" +
            "}"

            "QPushButton::pressed {" +
            "background-color: '#b23134'" +
            "}")

        self.ceasarButtonCopyText = QPushButton("Copy", self)
        self.ceasarButtonCopyText.setFont(Qt.QFont("Monospace", 9))
        self.ceasarButtonCopyText.setGeometry(665, 390, 35, 30)
        self.ceasarButtonCopyText.setCursor(QtCore.Qt.PointingHandCursor)
        self.ceasarButtonCopyText.clicked.connect(self.ceasar_copy_text)
        self.ceasarButtonCopyText.setStyleSheet("QPushButton {"
            "background-color: '#d8d8d8';" +
            "border: 2px solid black;" +
            "border-top-right-radius: 15px;" +
            "border-bottom-right-radius: 15px;"
            "}"

            "QPushButton::hover {" +
            "background-color: '#5c75b2';" +
            "border: 2px solid black;" +
            "}"

            "QPushButton::pressed {" +
            "background-color: '#3156b2';" +
            "}")

        self.ceasarButtonCleanText = QPushButton("Clean", self)
        self.ceasarButtonCleanText.setFont(Qt.QFont("Monospace", 9))
        self.ceasarButtonCleanText.setGeometry(622, 390, 45, 30)
        self.ceasarButtonCleanText.setCursor(QtCore.Qt.PointingHandCursor)
        self.ceasarButtonCleanText.clicked.connect(self.ceasar_clean_text)
        self.ceasarButtonCleanText.setStyleSheet("QPushButton {"
            "background-color: '#d8d8d8';" +
            "border: 2px solid black;" +
            "}"

            "QPushButton::hover {" +
            "background-color: '#b25c5e';" +
            "border: 2px solid black;" +
            "}"

            "QPushButton::pressed {" +
            "background-color: '#b23134'" +
            "}")

        self.ceasarButtonSwap = QPushButton(self)
        self.ceasarButtonSwap.setGeometry(702, 369, 32, 32)
        self.ceasarButtonSwap.clicked.connect(self.ceasar_swap)
        self.ceasarButtonSwap.setStyleSheet("QPushButton {" +
            "border: 0px solid black;" +
            "border-radius: 15px;" +
            "background-image: url(img/swap_white.png);" +
            "}"

            "QPushButton::hover {"
            "background-color: '#2b2b91';"
            "}"

            "QPushButton::pressed {"
            "background-color: '#2f2fce';"
            "}")

        # Decoration Line

        self.ceasarFrameDecorationLine = QFrame(self)
        self.ceasarFrameDecorationLine.setGeometry(40, 340, 681, 1)
        self.ceasarFrameDecorationLine.setStyleSheet("background-color: grey;")

    def ceasar_encrypt_decrypt_button(self):

        if self.ceasarLineEdit.text() == '' or self.ceasarLineEdit.text() == ' ':

            self.ceasarResult.setPlaceholderText('You didn\'t type anything')

        else:

            def get_operation(self):
                global operation
                operation = self.ceasarComboBoxOperations.currentText()
            get_operation(self)

            def get_typed_text(self):
                global text
                text = self.ceasarLineEdit.text()
            get_typed_text(self)

            def get_offset(self):
                global offset
                offset = int(self.ceasarComboBoxOffset.currentText())
                if (offset >= 1 and offset <= 26):
                    return offset
            get_offset(self)

            def cipher_message(self):
                if operation == 'Decrypt':
                    global offset
                    offset = -offset
                translated = ''
                for symbol in text:
                    if symbol.isalpha():
                        num = ord(symbol)
                        num += offset

                        if symbol.isupper():
                            if num > ord('Z'):
                                num -= 26
                            elif num < ord('A'):
                                num += 26
                        elif symbol.islower():
                            if num > ord('z'):
                                num -= 26
                            elif num < ord('a'):
                                num += 26
                        translated += chr(num)

                    else:
                        translated += symbol
                self.ceasarResult.setText(translated)
            cipher_message(self)

    def ceasar_clean_result(self):

        self.ceasarResult.setText("")

    def ceasar_clean_text(self):

        self.ceasarLineEdit.setText("")

    def ceasar_copy_result(self):

        copy = QApplication.clipboard()
        copy.clear(mode=copy.Clipboard)
        copy.setText(self.ceasarResult.text(), mode=copy.Clipboard)

    def ceasar_copy_text(self):

        copy = QApplication.clipboard()
        copy.clear(mode=copy.Clipboard)
        copy.setText(self.ceasarLineEdit.text(), mode=copy.Clipboard)

    def ceasar_swap(self):
        text_to_result = self.ceasarLineEdit.text()
        result_to_text = self.ceasarResult.text()
        self.ceasarResult.setText(text_to_result)
        self.ceasarLineEdit.setText(result_to_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogMain = DialogMain()
    dialogMain.show()
    sys.exit(app.exec_())
