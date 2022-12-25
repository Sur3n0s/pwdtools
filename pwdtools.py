import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import Qt, QtCore

# Password Tools v1.0

class DialogMain(QDialog):
    def __init__(self):
        super().__init__()

        # Main Window

        self.setWindowTitle("Password Tools")
        self.setFixedHeight(490)
        self.setFixedWidth(760)
        self.setStyleSheet("background-color: '#fcfcfc';")
        self.AllComponents()
        self.Ceasar()

    def AllComponents(self):

        # Frames

        self.FirstFrame = QFrame(self)
        self.FirstFrame.setGeometry(20, 20, 720, 90)
        self.FirstFrame.setStyleSheet("background-color: '#eadef7';" +
                                      "border: none;")

        self.SecondFrame = QFrame(self)
        self.SecondFrame.setGeometry(20, 130, 720, 150)
        self.SecondFrame.setStyleSheet("background-color: '#eadef7';" +
                                       "border: none;")

        self.ThirdFrame = QFrame(self)
        self.ThirdFrame.setGeometry(20, 300, 720, 170)
        self.ThirdFrame.setStyleSheet("background-color: '#eadef7';" +
            "border: none;")

        self.GreenLine = QFrame(self)
        self.GreenLine.setGeometry(20, 101, 720, 10)
        self.GreenLine.setStyleSheet("QFrame {"
            "background-color: green;" +
            "border: none;"
            "}")

        # LineEdit

        self.LineEditPasswd = QLineEdit("Password", self)
        self.LineEditPasswd.setGeometry(50, 40, 520, 40)
        self.LineEditPasswd.setReadOnly(True)
        self.LineEditPasswd.setCursor(QtCore.Qt.IBeamCursor)
        self.LineEditPasswd.setStyleSheet(" QLineEdit {"
            "background: '#eadef7';" +
            "color: black;" +
            "border: none;" +
            "font-size: 30px;" +
            "font-family: monospace;" +
            "}")

        # Labels

        self.LabelPasswdLen = QLabel("Password Lenght", self)
        self.LabelPasswdLen.setFont(Qt.QFont("Monospace", 10))
        self.LabelPasswdLen.setGeometry(40, 180, 130, 20)
        self.LabelPasswdLen.setStyleSheet("QLabel {"
            "color: rgb(0, 0, 0);" +
            "background-color: transparent;" +
            "}")

        self.LabelCustomize = QLabel("Customize your password", self)
        self.LabelCustomize.setFont(Qt.QFont("Monospace", 15))
        self.LabelCustomize.setGeometry(40, 130, 350, 40)
        self.LabelCustomize.setStyleSheet("QLabel {"
            "color: black;" +
            "background-color: transparent;" +
            "}")

        # Buttons

        self.btnGenerate = QPushButton(self)
        self.btnGenerate.setGeometry(660, 30, 64, 64)
        self.btnGenerate.setToolTip('<p style="color:black;">Refresh</p>')
        self.btnGenerate.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnGenerate.clicked.connect(self.main_check)
        self.btnGenerate.setStyleSheet("QPushButton {"
            "background-image: url(refresh.png);" +
            "border-radius: 30px;" +
            "background-color: none;" +
            "border: none;"
            "}"

            "QPushButton:hover {"
            "background-color: '#b7b7b7';"
            "}"

            "QPushButton:pressed {"
            "background-color: '#a4a4a4';"
            "}")

        self.btnCopy = QPushButton(self)
        self.btnCopy.setGeometry(590, 30, 64, 64)
        self.btnCopy.setToolTip('<p style="color: black;">Copy</p>')
        self.btnCopy.setCursor(QtCore.Qt.PointingHandCursor)
        self.btnCopy.clicked.connect(self.button_copy)
        self.btnCopy.setStyleSheet("QPushButton {"
            "background-image: url(copy.png);" +
            "border-radius: 5px;" +
            "background-color: none;" +
            "border: none;" +
            "}"

            "QPushButton:hover {"
            "background-color: '#b7b7b7';"
            "}"

            "QPushButton:pressed {"
            "background-color: '#a4a4a4';" +
            "}")

        # RadioButtons

        self.RadioBtnEasySay = QRadioButton("Easy to say", self)
        self.RadioBtnEasySay.setFont(Qt.QFont("Monospace", 10))
        self.RadioBtnEasySay.setGeometry(350, 180, 110, 22)
        self.RadioBtnEasySay.toggled.connect(self.radio_buttons_check)
        self.RadioBtnEasySay.setStyleSheet("color: black;" +
                                           "background-color: transparent;")

        self.RadioBtnEasyRead = QRadioButton("Easy to read", self)
        self.RadioBtnEasyRead.setFont(Qt.QFont("Monospace", 10))
        self.RadioBtnEasyRead.setGeometry(350, 210, 110, 22)
        self.RadioBtnEasyRead.toggled.connect(self.radio_buttons_check)
        self.RadioBtnEasyRead.setStyleSheet("color: black;" +
                                            "background-color: transparent;")

        self.RadioBtnAllChar = QRadioButton("All Characters", self)
        self.RadioBtnAllChar.setFont(Qt.QFont("Monospace", 10))
        self.RadioBtnAllChar.setGeometry(350, 240, 110, 22)
        self.RadioBtnAllChar.setChecked(True)
        self.RadioBtnAllChar.toggled.connect(self.radio_buttons_check)
        self.RadioBtnAllChar.setStyleSheet("color: black;" +
                                           "background-color: transparent;")

        # CheckBoxes

        self.checkBoxUppercase = QCheckBox("Uppercase", self)
        self.checkBoxUppercase.setFont(Qt.QFont("Monospace", 10))
        self.checkBoxUppercase.setGeometry(550, 180, 88, 22)
        self.checkBoxUppercase.setChecked(True)
        self.checkBoxUppercase.setStyleSheet("QCheckBox {"
            "color: black;" +
            "background-color: transparent;"
            "}")

        self.checkBoxLowcase = QCheckBox("Lowercase", self)
        self.checkBoxLowcase.setFont(Qt.QFont("Monospace", 10))
        self.checkBoxLowcase.setGeometry(550, 200, 88, 22)
        self.checkBoxLowcase.setChecked(True)
        self.checkBoxLowcase.setStyleSheet("QCheckBox {"
            "color: black;" +
            "background-color: transparent;"
            "}")

        self.checkBoxNum = QCheckBox("Numbers", self)
        self.checkBoxNum.setFont(Qt.QFont("Monospace", 10))
        self.checkBoxNum.setGeometry(550, 220, 88, 22)
        self.checkBoxNum.setStyleSheet("QCheckBox {"
            "color: black;" +
            "background-color: transparent;"
            "}")

        self.checkBoxSym = QCheckBox("Symbols", self)
        self.checkBoxSym.setFont(Qt.QFont("Monospace", 10))
        self.checkBoxSym.setGeometry(550, 240, 88, 22)
        self.checkBoxSym.setStyleSheet("QCheckBox {"
            "color: black;" +
            "background-color: transparent;"
            "}")

        # Slider

        self.SliderValue = QSlider(self,
                              value=10,
                              maximum=50,
                              minimum=1)
        self.SliderValue.setGeometry(100, 225, 160, 20)
        self.SliderValue.setOrientation(QtCore.Qt.Horizontal)
        self.SliderValue.setToolTip(str(self.SliderValue.value()))
        self.SliderValue.valueChanged.connect(self.slider_value_act)
        self.SliderValue.setStyleSheet("color: black;" +
                                       "background-color: '#eadef7';")

        # Spinbox

        self.spinBoxValue = QSpinBox(self,
                                value=10,
                                maximum=50,
                                minimum=1,
                                singleStep=1)
        self.spinBoxValue.setGeometry(40, 220, 52, 32)
        self.spinBoxValue.valueChanged.connect(self.spinbox_value_act)
        self.spinBoxValue.setStyleSheet("QSpinBox {"
            "color: black;" +
            "font-family: Arial Black;" +
            "font-size: 15px;" +
            "background-color: transparent;"
            "}")

        # Line

        self.DecorLine = QFrame(self)
        self.DecorLine.setGeometry(40, 170, 681, 1)
        self.DecorLine.setStyleSheet("background-color: grey;")

        #Functions

    def slider_value_act(self):
        current = self.SliderValue.value()
        self.spinBoxValue.setValue(current)
        self.main_check()

    def spinbox_value_act(self):
        current = self.spinBoxValue.value()
        self.SliderValue.setValue(current)
        self.main_check()

    def main_check(self):

        # Lists

        list_uppcase = ('QWERTYUIOPASDFGHJKLZXCVBNM')
        list_lowcase = ('qwertyuiopasdfghjklzxcvbnm')
        list_numbers = ('1234567890')
        list_symbols = ('!@#$%^&*()_=+-<>?/\|~')
        list_main = ''

        # Operations

        if self.checkBoxUppercase.isChecked() == True and self.checkBoxLowcase.isChecked() == True and self.checkBoxNum.isChecked() == True and self.checkBoxSym.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase + list_lowcase + list_numbers + list_symbols)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxUppercase.isChecked() == True and self.checkBoxLowcase.isChecked() == True and self.checkBoxNum.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase + list_lowcase + list_numbers)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxUppercase.isChecked() == True and self.checkBoxLowcase.isChecked() == True and self.checkBoxSym.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase + list_lowcase + list_symbols)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxUppercase.isChecked() == True and self.checkBoxNum.isChecked() == True and self.checkBoxSym.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase + list_numbers + list_symbols)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxLowcase.isChecked() == True and self.checkBoxNum.isChecked() == True and self.checkBoxSym.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_lowcase + list_numbers + list_symbols)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxUppercase.isChecked() == True and self.checkBoxLowcase.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase + list_lowcase)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxLowcase.isChecked() == True and self.checkBoxNum.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_lowcase + list_numbers)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxNum.isChecked() == True and self.checkBoxSym.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_numbers + list_symbols)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxUppercase.isChecked() == True and self.checkBoxNum.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase + list_numbers)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxLowcase.isChecked() == True and self.checkBoxSym.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_lowcase + list_symbols)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxUppercase.isChecked() == True and self.checkBoxSym.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase + list_symbols)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxSym.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_symbols)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxNum.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_numbers)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxUppercase.isChecked() == True:
            for x in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_uppcase)
                self.LineEditPasswd.setText(list_main)

        elif self.checkBoxLowcase.isChecked() == True:
            for i in range(self.spinBoxValue.value()):
                list_main = list_main + random.choice(list_lowcase)
                self.LineEditPasswd.setText(list_main)

        else:
            self.LineEditPasswd.setText('Please, choose valid option')

    def radio_buttons_check(self):
        if self.RadioBtnEasyRead.isChecked():
            self.checkBoxSym.setEnabled(False)
            self.checkBoxNum.setEnabled(False)
            self.checkBoxSym.setChecked(False)
            self.checkBoxNum.setChecked(False)
            self.checkBoxSym.setStyleSheet("QCheckBox {"
                "color: grey;" +
                "background-color: transparent;"
                "}")

            self.checkBoxNum.setStyleSheet("QCheckBox {"
                "color: grey;" +
                "background-color: transparent;"
                "}")

        elif self.RadioBtnEasySay.isChecked():
            self.checkBoxSym.setEnabled(False)
            self.checkBoxNum.setEnabled(False)
            self.checkBoxSym.setChecked(False)
            self.checkBoxNum.setChecked(False)
            self.checkBoxSym.setStyleSheet("QCheckBox {"
                "color: grey;" +
                "background-color: transparent;"
                "}")

            self.checkBoxNum.setStyleSheet("QCheckBox {"
                "color: grey;" +
                "background-color: transparent;"
                "}")

        else:
            self.checkBoxSym.setEnabled(True)
            self.checkBoxNum.setEnabled(True)
            self.checkBoxSym.setStyleSheet("QCheckBox {"
                "color: black;" +
                "background-color: transparent;"
                "}")

            self.checkBoxNum.setStyleSheet("QCheckBox {"
                "color: black;" +
                "background-color: transparent;"
                "}")

    def button_copy(self):
        copy = QApplication.clipboard()
        copy.clear(mode=copy.Clipboard)
        copy.setText(self.LineEditPasswd.text(), mode=copy.Clipboard)

    #########################
    ######CEASAR CIPHER######
    #########################

    def Ceasar(self):

        operations = ["Encrypt", "Decrypt"]
        offset = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]

        # Result Label

        self.ceasarResult = QLineEdit("Your message will be here", self)
        self.ceasarResult.setGeometry(40, 350, 647, 30)
        self.ceasarResult.setReadOnly(True)
        self.ceasarResult.setFont(Qt.QFont("Monospace", 10))
        self.ceasarResult.setAlignment(QtCore.Qt.AlignCenter)
        self.ceasarResult.setCursor(QtCore.Qt.IBeamCursor)
        self.ceasarResult.setStyleSheet("background-color: '#f4edfc';"
            "border: 2px solid black;" +
            "border-top-left-radius: 15px;" +
            "border-bottom-left-radius: 15px;" +
            "text-align: center;")

        # LineEdit

        self.ceasarLineEdit = QLineEdit("", self)
        self.ceasarLineEdit.setGeometry(40, 390, 647, 30)
        self.ceasarLineEdit.setFont(Qt.QFont("Monospace", 10))
        self.ceasarLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ceasarLineEdit.setMaxLength(100)
        self.ceasarLineEdit.setPlaceholderText("Type here something...")
        self.ceasarLineEdit.setStyleSheet("border: 2px solid black;" +
            "border-top-left-radius: 15px;" +
            "border-bottom-left-radius: 15px;" +
            "background-color: '#f4edfc';")

        # ComboBoxes

        self.ceasarComboOperations = QComboBox(self)
        self.ceasarComboOperations.setFont(Qt.QFont("Monospace", 9))
        self.ceasarComboOperations.setGeometry(100, 430, 140, 20)
        self.ceasarComboOperations.addItems(operations)

        self.ceasarComboOffset = QComboBox(self)
        self.ceasarComboOffset.setFont(Qt.QFont("Monospace", 9))
        self.ceasarComboOffset.setGeometry(290, 430, 60, 20)
        self.ceasarComboOffset.addItems(offset)

        # Labels

        self.ceasarSignLabel = QLabel("Ceasar Cipher", self)
        self.ceasarSignLabel.setFont(Qt.QFont("Monospace", 15))
        self.ceasarSignLabel.setGeometry(40, 300, 300, 40)
        self.ceasarSignLabel.setStyleSheet("QLabel {"
            "color: black;" +
            "background-color: none;"
            "}")

        self.ceasarOperaitonLabel = QLabel("Operation", self)
        self.ceasarOperaitonLabel.setGeometry(40, 430, 60, 20)
        self.ceasarOperaitonLabel.setFont(Qt.QFont("Monospace", 10))
        self.ceasarOperaitonLabel.setStyleSheet("background-color: none;")

        self.ceasarOffsetLabel = QLabel("Offset", self)
        self.ceasarOffsetLabel.setFont(Qt.QFont("Monospace", 10))
        self.ceasarOffsetLabel.setGeometry(250, 430, 40, 20)
        self.ceasarOffsetLabel.setStyleSheet("background-color: none;")

        # Buttons

        self.ceasarButtonEncrypt = QPushButton("Encrypt/Decrypt", self)
        self.ceasarButtonEncrypt.setFont(Qt.QFont("Monospace", 8))
        self.ceasarButtonEncrypt.setGeometry(360, 430, 280, 20)
        self.ceasarButtonEncrypt.setCursor(QtCore.Qt.PointingHandCursor)
        self.ceasarButtonEncrypt.clicked.connect(self.ceasar_encrypt_decrypt_btn)
        self.ceasarButtonEncrypt.setStyleSheet("QPushButton {"
            "border: 2px solid black;" +
            "border-radius: 10px;" +
            "background-color: '#f4edfc';"
            "}"

            "QPushButton::hover {" +
            "background-color: '#5fb25c';" +
            "border: 3px solid black;" +
            "}"

            "QPushButton::pressed {" +
            "background-color: '#24a320'" +
            "}")

        self.ceasarButtonClean = QPushButton("Clean", self)
        self.ceasarButtonClean.setFont(Qt.QFont("Monospace", 9))
        self.ceasarButtonClean.setGeometry(685, 350, 35, 30)
        self.ceasarButtonClean.setCursor(QtCore.Qt.PointingHandCursor)
        self.ceasarButtonClean.clicked.connect(self.ceasar_clean_result)
        self.ceasarButtonClean.setStyleSheet("QPushButton {"
            "background-color: '#f4edfc';" +
            "border: 2px solid black;" +
            "border-bottom-right-radius: 15px;" +
            "border-top-right-radius: 15px;"
            "}"

            "QPushButton::hover {" +
            "background-color: '#b25c5e';" +
            "border: 2px solid black;" +
            "}"

            "QPushButton::pressed {" +
            "background-color: '#b23134'" +
            "}")

        self.ceasarButtonClean2 = QPushButton("Clean", self)
        self.ceasarButtonClean2.setFont(Qt.QFont("Monospace", 9))
        self.ceasarButtonClean2.setGeometry(685, 390, 35, 30)
        self.ceasarButtonClean2.setCursor(QtCore.Qt.PointingHandCursor)
        self.ceasarButtonClean2.clicked.connect(self.ceasar_clean_text)
        self.ceasarButtonClean2.setStyleSheet("QPushButton {"
            "background-color: '#f4edfc';" +
            "border: 2px solid black;" +
            "border-top-right-radius: 15px;" +
            "border-bottom-right-radius: 15px;"
            "}"

            "QPushButton::hover {" +
            "background-color: '#b25c5e';" +
            "border: 2px solid black;" +
            "}"

            "QPushButton::pressed {" +
            "background-color: '#b23134'" +
            "}")

        self.ceasarButtonCopy = QPushButton("Copy Result", self)
        self.ceasarButtonCopy.setFont(Qt.QFont("Monospace", 8))
        self.ceasarButtonCopy.setGeometry(650, 430, 70, 20)
        self.ceasarButtonCopy.setCursor(QtCore.Qt.PointingHandCursor)
        self.ceasarButtonCopy.clicked.connect(self.ceasar_copy_btn)
        self.ceasarButtonCopy.setStyleSheet("QPushButton {"
            "background-color: '#f4edfc';" +
            "border: 2px solid black;" +
            "border-radius: 10px;"
            "}"

            "QPushButton::hover {" +
            "background-color: '#5c75b2';" +
            "}" +

            "QPushButton::pressed {" +
            "background-color: '#3156b2';" +
            "}")

        # Decoration Line

        self.ceasarDecorLine = QFrame(self)
        self.ceasarDecorLine.setGeometry(40, 340, 681, 1)
        self.ceasarDecorLine.setStyleSheet("background-color: grey;")

    def ceasar_encrypt_decrypt_btn(self):

        if self.ceasarLineEdit.text() == '' or self.ceasarLineEdit.text() == ' ':

            self.ceasarResult.setText('You didn\'t type anything')

        else:

            def get_operation(self):
                global operation
                operation = self.ceasarComboOperations.currentText()
            get_operation(self)

            def get_typed_text(self):
                global text
                text = self.ceasarLineEdit.text()
            get_typed_text(self)

            def get_offset(self):
                global offset
                offset = int(self.ceasarComboOffset.currentText())
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

        self.ceasarResult.setText("Your message will be here")

    def ceasar_clean_text(self):

        self.ceasarLineEdit.setText("")

    def ceasar_copy_btn(self):

        copy = QApplication.clipboard()
        copy.clear(mode=copy.Clipboard)
        copy.setText(self.ceasarResult.text(), mode=copy.Clipboard)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialogMain = DialogMain()
    dialogMain.show()
    sys.exit(app.exec_())
