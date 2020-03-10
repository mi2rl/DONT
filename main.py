import cv2
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from gui_viewer import GUIViewer

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    viewer = GUIViewer()
    viewer.show()
    
    app.exec_()
