# IMPORT PYQT5 CLASSES:
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox

# IMPORTS FUNCTIONS FROM FILES:
from Scanner import Scan, PrintTokens
from Parser import Parser
#Draw

# GLOBAL VARIABLES:
Initial_Text = '''{ Sample program in TINY language – computes factorial}
     read x;   {input an integer }
     if  0 < x   then     {  don’t compute if x <= 0 }
        fact  := 1;
        repeat 
           fact  := fact *  x;
            x  := x  -  1
        until  x  =  0;
        write  fact   {  output  factorial of x }
     end'''
Output_String = ""
Output_Type = ""
TokensList = []
File_Path = os.getcwd()
File_Name = "NOT_Named"

# GUI CLASS:
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1540, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Browse Button
        self.browse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.browse_btn.setGeometry(QtCore.QRect(1170, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.browse_btn.setFont(font)
        self.browse_btn.setObjectName("browse_btn")

        # Input Scroll Area
        self.input = QtWidgets.QScrollArea(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(30, 100, 631, 701))
        self.input.setWidgetResizable(True)
        self.input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.input.setObjectName("input")
        self.input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(20, 0, 629, 699))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        # Input Text Edit
        self.input_tedt = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.input_tedt.setGeometry(QtCore.QRect(30, 10, 611, 681))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.input_tedt.setFont(font)
        self.input_tedt.setText("")
        self.input_tedt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.input_tedt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_tedt.setObjectName("input_tedt")
        self.verticalLayout.addWidget(self.input_tedt)
        self.input.setWidget(self.scrollAreaWidgetContents)
        global Initial_Text
        self.input_tedt.setText(Initial_Text)

        # Output Scroll Area
        self.output = QtWidgets.QScrollArea(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(690, 100, 631, 701))
        self.output.setWidgetResizable(True)
        self.output.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.output.setObjectName("output")
        self.output.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 629, 699))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Output Label
        self.output_lbl = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.output_lbl.setGeometry(QtCore.QRect(10, 10, 611, 681))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.output_lbl.setFont(font)
        self.output_lbl.setText("")
        self.output_lbl.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.output_lbl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.output_lbl.setObjectName("output_lbl")
        self.verticalLayout_2.addWidget(self.output_lbl)
        self.output.setWidget(self.scrollAreaWidgetContents_2)

        # Browse Line Edit
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 10, 1131, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        # Scan Button
        self.Scan_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Scan_btn.setGeometry(QtCore.QRect(1340, 100, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Scan_btn.setFont(font)
        self.Scan_btn.setObjectName("Scan_btn")

        # Parse Button
        self.Parse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Parse_btn.setGeometry(QtCore.QRect(1340, 175, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Parse_btn.setFont(font)
        self.Parse_btn.setObjectName("Parse_btn")

        # Label Pointing to Input
        self.InputPointing_lbl = QtWidgets.QLabel(self.centralwidget)
        self.InputPointing_lbl.setGeometry(QtCore.QRect(10, 810, 621, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.InputPointing_lbl.setFont(font)
        self.InputPointing_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.InputPointing_lbl.setObjectName("InputPointing_lbl")

        # Label Pointing to Output
        self.OutputPointing_lbl = QtWidgets.QLabel(self.centralwidget)
        self.OutputPointing_lbl.setGeometry(QtCore.QRect(680, 810, 631, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.OutputPointing_lbl.setFont(font)
        self.OutputPointing_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.OutputPointing_lbl.setObjectName("OutputPointing_lbl")

        # Save Button
        self.Save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Save_btn.setGeometry(QtCore.QRect(1340, 740, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.Save_btn.setFont(font)
        self.Save_btn.setObjectName("Save_btn")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1549, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TINT-Language Scanner"))
        self.InputPointing_lbl.setText(_translate("MainWindow", "Input"))
        self.OutputPointing_lbl.setText(_translate("MainWindow", "Output"))
        self.browse_btn.setText(_translate("MainWindow", "Browse"))
        self.Scan_btn.setText(_translate("MainWindow", "Scan"))
        self.Parse_btn.setText(_translate("MainWindow", "Parse"))
        self.Save_btn.setText(_translate("MainWindow", "Save"))
        self.browse_btn.clicked.connect(self.browse_handler)
        self.Scan_btn.clicked.connect(self.scan_handler)
        self.Save_btn.clicked.connect(self.save_handler)
        self.Parse_btn.clicked.connect(self.parse_handler)

    def browse_handler(self):
        self.open_dialog_box()

    def scan_handler(self):
        global Output_String
        global Output_Type
        global TokensList
        Output_Type = "Scan"
        TokensList = Scan(self.input_tedt.toPlainText())
        if not TokensList:
            # Message Box
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Error")
            msg.setInformativeText(f"No Input Code")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            ReturnList = PrintTokens(TokensList)
            Output_String = ReturnList [1]
            self.output_lbl.setText(Output_String)
            if ReturnList[0] == True:
                # Message Box
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Lexical Error")
                msg.setInformativeText(f"This TINY Code has a Lexical Error")
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()


    def parse_handler(self):
        global Output_String
        global Output_Type
        global TokensList
        Output_Type = "Scan"
        TokensList = Scan(self.input_tedt.toPlainText())
        if not TokensList:
            # Message Box
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Error")
            msg.setInformativeText(f"No Input Code")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            ReturnList = PrintTokens(TokensList)
            Output_String = ReturnList [1]
            self.output_lbl.setText(Output_String)
            if ReturnList[0] == True:
                # Message Box
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Lexical Error")
                msg.setInformativeText(f"This TINY Code has a Lexical Error")
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            else:
                Parse_OBJ = Parser()
                Parse_OBJ.set_tokens_list_and_code_list(TokensList)
                ParseRet = Parse_OBJ.run()
                if ParseRet[0] == True:
                    # Message Box
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Syntax Error")
                    Info = "This TINY Code has a Syntax Error\n"
                    for Token in ParseRet[1]:
                        Info = Info + f'LINE# {Token[2]} Syntax Error with Token "{Token[1]}"\n'
                    msg.setInformativeText(Info)
                    msg.setWindowTitle("Error")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
                else:
                    nodes_list = Parse_OBJ.nodes_table
                    edges_list = Parse_OBJ.edges_table
                    # Add Nodes to Graph

                    # Add Edges to Graph

                    Parse_OBJ.clear_tables()


    def save_handler(self):
        global Output_String
        global Output_Type
        global File_Path
        global File_Name
        if Output_Type == "Scan":
            file = open(f"{File_Path}//{File_Name}scan", "w")
            file.write(Output_String)
            file.close()
            # Message Box
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Saved")
            msg.setInformativeText(f"Scanned Tokens are Saved in '{File_Path}' \nIt's name is {File_Name}scan")
            msg.setWindowTitle("Information")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

    def open_dialog_box(self):
        global File_Path
        global File_Name
        File_Path = ""
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        self.output_lbl.setText("")
        self.lineEdit.setText(path)
        with open(path, "r") as f:
            Input_String = f.read()
            self.input_tedt.setText(Input_String)
            Split_Path = path.split('/')
            File_Name = Split_Path[-1]
            for i in range(len(Split_Path) - 1):
                File_Path = File_Path + Split_Path[i] + "/"


# MAIN:
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
