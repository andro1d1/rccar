from PySide6.QtCore import QUrl
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt
import control
import keyboard

class Widgets(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Window title")
        self.widget = QWidget(self)

        self.webview = QWebEngineView()
        self.webview.load(QUrl("http://178.176.46.90:8002/index.html"))
        #self.webview.load(QUrl("http://192.168.10.101:8002/index.html"))
        self.webview.setFixedSize(1920, 1080)

        self.additional_widget = QLabel(self)
        self.additional_widget.setFixedSize(650, 400)
        self.additional_widget.setStyleSheet("background-color: transparent;")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.webview)
        self.layout.addWidget(self.additional_widget, alignment=Qt.AlignBottom | Qt.AlignLeft)

        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        keyboard.on_press_key("w", self.check_keys)
        keyboard.on_press_key("a", self.check_keys)
        keyboard.on_press_key("s", self.check_keys)
        keyboard.on_press_key("d", self.check_keys)
        keyboard.on_release(self.release_keys)

        self.keys_pressed = set()
        
        self.car = control.ControlCar()
    
    def update_additional_widget(self, image_path):
        pixmap = QPixmap(image_path)
        self.additional_widget.setPixmap(pixmap)

    def check_keys(self, event):
        self.keys_pressed.add(event.name)
        self.car.control_car(self.keys_pressed)

    def release_keys(self, event):
        if event.name in self.keys_pressed:
            if event.name in ("a", "d"):
                self.car.control_car(("a", "d"))
            if event.name in ("w", "s"):
                self.car.control_car(("w", "s"))
            self.keys_pressed.remove(event.name)