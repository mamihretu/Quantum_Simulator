from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QPalette, QColor, QDrag, QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QPushButton, QSizePolicy, QWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(800,500)        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setAutoFillBackground(False)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAcceptDrops(True)
        self.centralwidget.setObjectName("centralwidget")

        self.clearCircuit = QtWidgets.QPushButton(self.centralwidget)
        self.clearCircuit.setGeometry(QtCore.QRect(600, 290, 161, 131))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(18)
        font.setItalic(False)
        self.clearCircuit.setFont(font)
        self.clearCircuit.setMouseTracking(False)
        self.clearCircuit.setObjectName("clearCircuit")

        self.runCircuit = QtWidgets.QPushButton(self.centralwidget)
        self.runCircuit.setGeometry(QtCore.QRect(600, 150, 161, 131))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi")
        font.setPointSize(18)
        font.setItalic(False)
        self.runCircuit.setFont(font)
        self.runCircuit.setMouseTracking(False)
        self.runCircuit.setObjectName("runCircuit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.make_lines()
        self.make_buttons()
        self.make_comboBoxes()
        self.make_labels() 

        self.comboBoxList = [self.comboBox,self.comboBox_2,self.comboBox_3,self.comboBox_4,self.comboBox_5,self.comboBox_6
                        ,self.comboBox_7,self.comboBox_8,self.comboBox_9,self.comboBox_10,self.comboBox_11,self.comboBox_12
                        ,self.comboBox_13,self.comboBox_14,self.comboBox_15,self.comboBox_16,self.comboBox_17,self.comboBox_18
                        ,self.comboBox_19,self.comboBox_20,self.comboBox_21,self.comboBox_22,self.comboBox_23,self.comboBox_24
                        ,self.comboBox_25,self.comboBox_26,self.comboBox_27,self.comboBox_28,self.comboBox_29,self.comboBox_30
                        ,self.comboBox_31,self.comboBox_32,self.comboBox_33,self.comboBox_34,self.comboBox_35,self.comboBox_36]

        self.gateList = ["","X","Y","Z","H","CX","RX","RY","RZ","M"]
        self.add_Gate_List()

        self.runCircuit.clicked.connect(self.run)
        self.clearCircuit.clicked.connect(self.clear)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        

    def make_lines(self):
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(60, 150, 521, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")        
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(60, 200, 521, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(60, 250, 521, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(60, 300, 521, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(60, 350, 521, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(60, 400, 521, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")

    def make_buttons(self):
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 140, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 190, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 240, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 290, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(10, 340, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(10, 390, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")

    def make_comboBoxes(self):
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(80, 150, 41, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(160, 150, 41, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(240, 150, 41, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(320, 150, 41, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(400, 150, 41, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setGeometry(QtCore.QRect(480, 150, 41, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_7 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_7.setGeometry(QtCore.QRect(80, 200, 41, 22))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_8 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_8.setGeometry(QtCore.QRect(160, 200, 41, 22))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_9 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_9.setGeometry(QtCore.QRect(240, 200, 41, 22))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_10 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_10.setGeometry(QtCore.QRect(320, 200, 41, 22))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_11 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_11.setGeometry(QtCore.QRect(400, 200, 41, 22))
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_12 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_12.setGeometry(QtCore.QRect(480, 200, 41, 22))
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_13 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_13.setGeometry(QtCore.QRect(80, 250, 41, 22))
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_14 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_14.setGeometry(QtCore.QRect(160, 250, 41, 22))
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_15 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_15.setGeometry(QtCore.QRect(240, 250, 41, 22))
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_16 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_16.setGeometry(QtCore.QRect(320, 250, 41, 22))
        self.comboBox_16.setObjectName("comboBox_16")
        self.comboBox_17 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_17.setGeometry(QtCore.QRect(400, 250, 41, 22))
        self.comboBox_17.setObjectName("comboBox_17")
        self.comboBox_18 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_18.setGeometry(QtCore.QRect(480, 250, 41, 22))
        self.comboBox_18.setObjectName("comboBox_18")
        self.comboBox_19 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_19.setGeometry(QtCore.QRect(80, 300, 41, 22))
        self.comboBox_19.setObjectName("comboBox_19")
        self.comboBox_20 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_20.setGeometry(QtCore.QRect(160, 300, 41, 22))
        self.comboBox_20.setObjectName("comboBox_20")
        self.comboBox_21 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_21.setGeometry(QtCore.QRect(240, 300, 41, 22))
        self.comboBox_21.setObjectName("comboBox_21")
        self.comboBox_22 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_22.setGeometry(QtCore.QRect(320, 300, 41, 22))
        self.comboBox_22.setObjectName("comboBox_22")
        self.comboBox_23 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_23.setGeometry(QtCore.QRect(400, 300, 41, 22))
        self.comboBox_23.setObjectName("comboBox_23")
        self.comboBox_24 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_24.setGeometry(QtCore.QRect(480, 300, 41, 22))
        self.comboBox_24.setObjectName("comboBox_24")
        self.comboBox_25 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_25.setGeometry(QtCore.QRect(80, 350, 41, 22))
        self.comboBox_25.setObjectName("comboBox_25")
        self.comboBox_26 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_26.setGeometry(QtCore.QRect(160, 350, 41, 22))
        self.comboBox_26.setObjectName("comboBox_26")
        self.comboBox_27 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_27.setGeometry(QtCore.QRect(240, 350, 41, 22))
        self.comboBox_27.setObjectName("comboBox_27")
        self.comboBox_28 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_28.setGeometry(QtCore.QRect(320, 350, 41, 22))
        self.comboBox_28.setObjectName("comboBox_28")
        self.comboBox_29 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_29.setGeometry(QtCore.QRect(400, 350, 41, 22))
        self.comboBox_29.setObjectName("comboBox_29")
        self.comboBox_30 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_30.setGeometry(QtCore.QRect(480, 350, 41, 22))
        self.comboBox_30.setObjectName("comboBox_30")
        self.comboBox_31 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_31.setGeometry(QtCore.QRect(80, 400, 41, 22))
        self.comboBox_31.setObjectName("comboBox_31")
        self.comboBox_32 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_32.setGeometry(QtCore.QRect(160, 400, 41, 22))
        self.comboBox_32.setObjectName("comboBox_32")
        self.comboBox_33 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_33.setGeometry(QtCore.QRect(240, 400, 41, 22))
        self.comboBox_33.setObjectName("comboBox_33")
        self.comboBox_34 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_34.setGeometry(QtCore.QRect(320, 400, 41, 22))
        self.comboBox_34.setObjectName("comboBox_34")
        self.comboBox_35 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_35.setGeometry(QtCore.QRect(400, 400, 41, 22))
        self.comboBox_35.setObjectName("comboBox_35")
        self.comboBox_36 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_36.setGeometry(QtCore.QRect(480, 400, 41, 22))
        self.comboBox_36.setObjectName("comboBox_36")

    def make_labels(self):
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 0, 711, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 59, 541, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowTitle("SimQ")
        MainWindow.setWindowIcon(QIcon("..\\Gui.PNG"))
        self.clearCircuit.setText(_translate("MainWindow", "Clear Circuit"))
        self.runCircuit.setText(_translate("MainWindow", "Run Circuit"))
        self.pushButton_9.setText(_translate("MainWindow", "|0>"))
        self.pushButton_10.setText(_translate("MainWindow", "|0>"))
        self.pushButton_11.setText(_translate("MainWindow", "|0>"))
        self.pushButton_12.setText(_translate("MainWindow", "|0>"))
        self.pushButton_13.setText(_translate("MainWindow", "|0>"))
        self.pushButton_14.setText(_translate("MainWindow", "|0>"))
        self.label.setText(_translate("MainWindow", "                   SimQ"))
        self.label_2.setText(_translate("MainWindow", "               A Toy Quantum Simulator"))


    def add_Gate_List(self):
        for box in self.comboBoxList:
            box.addItems(self.gateList)

    def clear(self):
        for box in self.comboBoxList:
            box.setCurrentText("")

    def run(self):

        from quantumSimulator  import QuantumSimulator
        from quantumCircuit import QuantumCircuit
        from math import cos,sin,pi
        
        qc = QuantumCircuit(6)


        for i, box in enumerate(self.comboBoxList):

            if 0<=i<6: 
                if box.currentText() == "":
                    continue                             
                if box.currentText() == "X":
                    qc.x(0)
                if box.currentText() == "Y":
                    qc.y(0)                
                if box.currentText() == "Z":
                    qc.z(0)
                if box.currentText() == "H":
                    qc.h(0)                    
                if box.currentText() == "CX":
                    qc.cx(0,1)
                if box.currentText() == "RX":
                    qc.rx(0,pi)
                if box.currentText() == "RY":
                    qc.ry(0,pi)
                if box.currentText() == "RZ":
                    qc.rz(0,pi)
                if box.currentText() == "M":
                    qc.m(0,1)

            elif 6<=i<12:
                if box.currentText() == "":
                    continue                   
                if box.currentText() == "X":
                    qc.x(1)
                if box.currentText() == "Y":
                    qc.y(1)                
                if box.currentText() == "Z":
                    qc.z(1)
                if box.currentText() == "H":
                    qc.h(1)                    
                if box.currentText() == "CX":
                    qc.cx(1,2)
                if box.currentText() == "RX":
                    qc.rx(1,pi)
                if box.currentText() == "RY":
                    qc.ry(1,pi)
                if box.currentText() == "RZ":
                    qc.rz(1,pi)
                if box.currentText() == "M":
                    qc.m(1,4)               
            elif 12<=i<18:
                if box.currentText() == "":
                    continue                   
                if box.currentText() == "X":
                    qc.x(2)
                if box.currentText() == "Y":
                    qc.y(2)                
                if box.currentText() == "Z":
                    qc.z(2)
                if box.currentText() == "H":
                    qc.h(2)                    
                if box.currentText() == "CX":
                    qc.cx(2,3)
                if box.currentText() == "RX":
                    qc.rx(2,pi)
                if box.currentText() == "RY":
                    qc.ry(2,pi)
                if box.currentText() == "RZ":
                    qc.rz(2,pi)
                if box.currentText() == "M":
                    qc.m(2,3)
            elif 18<=i<24:
                if box.currentText() == "":
                    continue                   
                if box.currentText() == "X":
                    qc.x(3)
                if box.currentText() == "Y":
                    qc.y(3)                
                if box.currentText() == "Z":
                    qc.z(3)
                if box.currentText() == "H":
                    qc.h(3)                    
                if box.currentText() == "CX":
                    qc.cx(3,4)
                if box.currentText() == "RX":
                    qc.rx(3,pi)
                if box.currentText() == "RY":
                    qc.ry(3,pi)
                if box.currentText() == "RZ":
                    qc.rz(3,pi)
                if box.currentText() == "M":
                    qc.m(3,4)
            elif 24<=i<30:
                if box.currentText() == "":
                    continue                   
                if box.currentText() == "X":
                    qc.x(4)
                if box.currentText() == "Y":
                    qc.y(4)                
                if box.currentText() == "Z":
                    qc.z(4)
                if box.currentText() == "H":
                    qc.h(4)                    
                if box.currentText() == "CX":
                    qc.cx(4,5)
                if box.currentText() == "RX":
                    qc.rx(4,pi)
                if box.currentText() == "RY":
                    qc.ry(4,pi)
                if box.currentText() == "RZ":
                    qc.rz(4,pi)
                if box.currentText() == "M":
                    qc.m(4,3)
            elif 30<=i<36:
                if box.currentText() == "":
                    continue                   
                if box.currentText() == "X":
                    qc.x(5)
                if box.currentText() == "Y":
                    qc.y(5)                
                if box.currentText() == "Z":
                    qc.z(5)
                if box.currentText() == "H":
                    qc.h(5)                    
                if box.currentText() == "CX":
                    qc.cx(5,0)
                if box.currentText() == "RX":
                    qc.rx(5,pi)
                if box.currentText() == "RY":
                    qc.ry(5,pi)
                if box.currentText() == "RZ":
                    qc.rz(5,pi)
                if box.currentText() == "M":
                    qc.m(5,1)

        quantumSimulator =  QuantumSimulator(qc)
        result = quantumSimulator.run(1024, "counts")
        print(result)

        import matplotlib.pyplot as plt
        
        possibilities = result.keys()
        outcomes = result.values()
        plt.bar(possibilities,outcomes)
        plt.xticks(rotation=80, ha='right')
        plt.show()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # Force the style to be the same on all OSs:
    app.setStyle("Fusion")

    # Now use a palette to switch to dark colors:
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.green)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.green)
    palette.setColor(QPalette.Text, Qt.green)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.green)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
