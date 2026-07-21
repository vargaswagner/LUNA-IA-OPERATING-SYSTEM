from PySide6.QtGui import (
    QPainter,
    QRadialGradient,
    QColor
)



class Bloom:


    def draw(
        self,
        canvas,
        center,
        radius
    ):


        painter=QPainter(canvas)


        gradient=QRadialGradient(
            center,
            radius
        )


        gradient.setColorAt(
            0,
            QColor(
                0,
                255,
                255,
                80
            )
        )


        gradient.setColorAt(
            0.5,
            QColor(
                0,
                100,
                255,
                30
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
            gradient
        )


        painter.drawEllipse(
            center,
            radius,
            radius
        )


        painter.end()