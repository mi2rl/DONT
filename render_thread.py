import cv2
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from action_classifier import ActionClassifier

class RenderThread(QThread):
    status = None
    action_classifier = ActionClassifier(model_path='weights/i3d_rgb_multi_class.pth')
    changePixmap = pyqtSignal(QImage)
    
    action_result = pyqtSignal(str)

    def run(self):
        cap = cv2.VideoCapture(0)
        #cap = cv2.VideoCapture('/home/sungman/Videos/Short_Input.avi')
        while cap.isOpened():
            ret, frame = cap.read()

            if ret:
                rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rgb_img = cv2.resize(rgb_img, (480,320))
                h, w, ch = rgb_img.shape

                if self.status is False:
                    result = self.action_classifier.run(rgb_img)
                    self.action_result.emit(result)

            bytesPerLine = ch * w
            convertToQtFormat = QImage(rgb_img.data, w, h, bytesPerLine, QImage.Format_RGB888)
            p = convertToQtFormat.scaled(480,320, Qt.KeepAspectRatio)
            self.changePixmap.emit(p)
            
    
    def setStatus(self, status):
        self.status = status

    def get_action_result(self):
        return self.action_result

        

