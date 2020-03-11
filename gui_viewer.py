'''
##### DO Not Touch your face ver.0.2

### Medical Imaging & Intelligent Reality Lab (MI2RL) @ Asan Medical Center(AMC)
# MI2RL website : https://www.mi2rl.co/
# AMC : http://www.amc.seoul.kr/asan/main.do

### Developer
# Sungman Cho : dev.sungman@gmail.com
# Minjee Kim : minjeekim00@gmail.com
# Taehyeong Kim : kimtaehyeong62@gmail.com
# Junmyung Choi : jm5901@gmail.com
# Namkug Kim : namkugkim@gmail.com

### Data contributor
# MI2RL researchers
# Dongwoo Seo, Emergency Medicine@AMC 
# Namkug Kim, Convergence Medicine@AMC

### references
# I3D Network (https://github.com/hassony2/kinetics_i3d_pytorch)

#####
'''

import cv2
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from render_thread import RenderThread

### For viewing GUI
class GUIViewer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.position = self._get_location()
        
        # TODO : connect ConfigViewer to main GUIviewer
        self.config_window = ConfigboxViewer()
        self.video_viewer = VideoViewer()

        # Rendering Thread for getting Webcam's image
        self.render_thread = RenderThread(self)
        self.render_thread.action_result.connect(self.update_touching_status)
        self.render_thread.changePixmap.connect(self.setImage)

        self.render_thread.start()
        
    # GUI Position Setting
    def _get_location(self):
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()
        fg = self.frameGeometry()

        widget = self.geometry()
        x = ag.width() - widget.width()
        y = 2 * ag.height() - sg.height() - widget.width()

        x = sg.width() - fg.width()
        y = sg.height() - fg.height()
        
        return (x,y, fg.width(), fg.height())

    def initUI(self):
        self.status_label = QLabel('행동 인식 기능: 꺼짐')
        self.touching_status = QLabel('알림 : ')

        ### Button Layout. 
        self.config_btn = QPushButton('설정')
        self.config_btn.clicked.connect(self.config_clicked)

        self.view_btn = QPushButton('카메라')
        self.view_btn.clicked.connect(self.view_clicked)

        self.start_btn = QPushButton('시작')
        self.start_btn.clicked.connect(self.start_clicked)

        self.pause_btn = QPushButton('중지')
        self.pause_btn.clicked.connect(self.pause_clicked)
        ### 
        
        v_layout = QtWidgets.QVBoxLayout()
        v_layout.addWidget(self.status_label)
        v_layout.addWidget(self.touching_status)
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(self.start_btn)
        h_layout.addWidget(self.pause_btn)
        h_layout.addWidget(self.config_btn)
        h_layout.addWidget(self.view_btn)
        v_layout.addLayout(h_layout)
        self.setLayout(v_layout)
        
        self.setGeometry(1440, 1030, 500, 50)

        self.setWindowTitle('얼굴을 만지지 마세요 (ver.0.2)')
        
        
    def config_clicked(self):
        self.config_window.showModal()

    def view_clicked(self):
        self.video_viewer.showModal()

    def start_clicked(self):
        self.status_label.setText('행동 인식 기능: 켜짐')
        self.render_thread.setStatus(False) 

        
    def pause_clicked(self):
        self.status_label.setText('행동 인식 기능: 꺼짐')
        
        self.render_thread.start()
        self.render_thread.setStatus(True)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '닫기', '프로그램을 종료하시겠습니까?',
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            self.deleteLater()
            event.accept()

        else:
            event.ignore()

    @pyqtSlot(QImage)
    def setImage(self, image):
        self.video_viewer.image_label.setPixmap(QPixmap.fromImage(image))
        

    @pyqtSlot(str)
    def update_touching_status(self, message):
        self.touching_status.setText('알림 : {}'.format(message))

### For viewing webCAM
class VideoViewer(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.isRun = False

    def initUI(self):
        self.setWindowTitle('카메라')
        
        # 추후 백그라운드 실행되도록 변경
        self.image_label = QLabel(self)
        v_layout = QtWidgets.QVBoxLayout()
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(self.image_label)
        v_layout.addLayout(h_layout)
        self.setLayout(v_layout)

        self.setGeometry(1440, 655, 480, 320)

    def showModal(self):
        return super().exec_()

### For viewing Config Box
class ConfigboxViewer(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('설정')
        
        self.label = QLabel('알람을 받을 행동을 체크해주세요')
        
        ### Button Layout

        self.mask_cb = QCheckBox('마스크 착용', self)
        self.mask_cb.stateChanged.connect(self.check_mask)
        
        self.chin_cb = QCheckBox('턱 괴기', self)
        self.chin_cb.stateChanged.connect(self.check_chin)
        
        self.eye_cb = QCheckBox('눈 비비기', self)
        self.eye_cb.stateChanged.connect(self.check_eye)
        
        self.hair_cb = QCheckBox('머리 만지기', self)
        self.hair_cb.stateChanged.connect(self.check_hair)
        
        self.phone_cb = QCheckBox('핸드폰 만지기', self)
        self.phone_cb.stateChanged.connect(self.check_phone)
        
        self.call_cb = QCheckBox('전화 받기', self)
        self.call_cb.stateChanged.connect(self.check_call)
        
        self.eye_glass_cb = QCheckBox('안경 만지기', self)
        self.eye_glass_cb.stateChanged.connect(self.check_eye_glass)
        
        self.water_cb = QCheckBox('물마시기', self)
        self.water_cb.stateChanged.connect(self.check_water)
        
        self.check_btn = QPushButton('적용')
        self.check_btn.clicked.connect(self.check_clicked)

        v_layout = QtWidgets.QVBoxLayout()
        v_layout.addWidget(self.mask_cb)
        v_layout.addWidget(self.chin_cb)
        v_layout.addWidget(self.eye_cb)
        v_layout.addWidget(self.hair_cb)
        v_layout.addWidget(self.phone_cb)
        v_layout.addWidget(self.call_cb)
        v_layout.addWidget(self.eye_glass_cb)
        v_layout.addWidget(self.water_cb)
        v_layout.addWidget(self.check_btn)
        self.setLayout(v_layout)

        self.setGeometry(1295, 660, 140, 450)

    def check_mask(self):
        print('check_mask clicked')

    def check_chin(self):
        print('check_chin clicked')

    def check_eye(self):
        print('check_eye clicked')

    def check_hair(self):
        print('check_hair clicked')

    def check_phone(self):
        print('check_phone clicked')

    def check_call(self):
        print('check_call clicked')
    
    def check_eye_glass(self):
        print('check_eye_glass clicked')
    
    def check_water(self):
        print('check_water clicked')

    def check_clicked(self):
        print('check btn clicked')
        self.accept()
    
    def showModal(self):
        return super().exec_()

