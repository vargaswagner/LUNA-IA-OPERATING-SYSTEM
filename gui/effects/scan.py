import time



class Scan:


    def __init__(self):

        self.position=0



    def draw(
        self,
        canvas
    ):

        from PySide6.QtGui import (
            QPainter,
            QColor
        )


        painter=QPainter(canvas)


        self.position+=3


        if self.position>canvas.height():

            self.position=0



        painter.setPen(
            QColor(
                0,
                220,
                255,
                35
            )
        )


        painter.drawLine(
            0,
            self.position,
            canvas.width(),
            self.position
        )


        painter.end()