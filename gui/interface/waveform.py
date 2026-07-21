import math
import time


from PySide6.QtGui import (
    QPainter,
    QColor
)



class Waveform:


    def draw(
        self,
        canvas
    ):


        painter = QPainter(canvas)


        painter.setRenderHint(
            QPainter.Antialiasing
        )


        center = (
            canvas.rect()
            .center()
        )


        t=time.time()



        painter.setPen(
            QColor(
                0,
                230,
                255,
                150
            )
        )


        for i in range(80):


            angle = (
                i/80
                *
                math.pi*2
            )


            radius = (
                230
                +
                math.sin(
                    t*5+i
                )
                *
                15
            )


            x = (
                center.x()
                +
                math.cos(angle)
                *
                radius
            )


            y = (
                center.y()
                +
                math.sin(angle)
                *
                radius
            )


            painter.drawPoint(
                x,
                y
            )


        painter.end()