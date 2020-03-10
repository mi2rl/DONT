import cv2
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class GUIViewer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    @pyqtSlot(QImage)
    def setImage(self, image):
        self.image_label.setPixmap(QPixmap.fromImage(image))

    def initUI(self):
        self.image_label = QLabel(self)

        ### Layout. 
        #self.start_btn = QtWidgets.QPushButton('Start')
        #self.start_btn.clicked.connect(self.start_button_clicked)

        self.label = QLabel()

        v_layout = QtWidgets.QVBoxLayout()
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(viewer)
        v_layout.addLayout(h_layout)
        v_layout.addWidget(start_btn)

        layout_widget = QtWidgets.QWidget()
        self.setLayout(v_layout)

        
        th = RenderThread(self)
        th.changePixmap.connect(self.setImage)
        th.start()

        

