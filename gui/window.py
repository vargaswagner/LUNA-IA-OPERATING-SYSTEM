from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt

from gui.canvas import JarvisCanvas



class JarvisWindow(QMainWindow):


    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "JARVIS AI"
        )


        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )


        self.setAttribute(
            Qt.WA_TranslucentBackground
        )


        self.resize(
            900,
            700
        )


        self.canvas = JarvisCanvas()


        self.setCentralWidget(
            self.canvas
        )


        self.drag = None



    def mousePressEvent(self,event):

        if event.button() == Qt.LeftButton:

            self.drag = (
                event.globalPosition()
                .toPoint()
                -
                self.pos()
            )



    def mouseMoveEvent(self,event):

        if self.drag:

            self.move(
                event.globalPosition()
                .toPoint()
                -
                self.drag
            )