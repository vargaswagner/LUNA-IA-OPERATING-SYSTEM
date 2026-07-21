from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer,Qt

from gui.renderer.renderer import Renderer



class JarvisCanvas(QWidget):


    def __init__(self):

        super().__init__()


        self.setAttribute(
            Qt.WA_TranslucentBackground
        )


        self.renderer = Renderer()



        timer = QTimer(self)

        timer.timeout.connect(
            self.update
        )


        timer.start(16)



    def paintEvent(self,event):

        self.renderer.draw(
            self
        )