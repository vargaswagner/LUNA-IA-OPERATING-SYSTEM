import time
import math

from PySide6.QtGui import (
    QColor,
    QBrush,
    QRadialGradient
)

from PySide6.QtCore import Qt



class EnergyCore:


    def __init__(self):

        self.start = time.time()



    def draw(
        self,
        painter,
        center
    ):


        t = time.time()-self.start


        pulse = (
            math.sin(t*3)
            +
            1
        ) / 2



        radius = (
            45
            +
            pulse*15
        )



        gradient = QRadialGradient(

            center,

            radius*3

        )


        gradient.setColorAt(
            0,
            QColor(
                255,
                255,
                255,
                255
            )
        )


        gradient.setColorAt(
            0.15,
            QColor(
                0,
                255,
                255,
                240
            )
        )


        gradient.setColorAt(
            0.5,
            QColor(
                0,
                100,
                255,
                80
            )
        )


        gradient.setColorAt(
            1,
            QColor(
                0,
                0,
                0,
                0
            )
        )


        painter.setBrush(
            QBrush(
                gradient
            )
        )


        painter.setPen(
            Qt.NoPen
        )


        painter.drawEllipse(

            center,

            int(radius*3),

            int(radius*3)

        )



        painter.setBrush(

            QColor(
                255,
                255,
                255
            )

        )


        painter.drawEllipse(

            center,

            int(radius/2),

            int(radius/2)

        )