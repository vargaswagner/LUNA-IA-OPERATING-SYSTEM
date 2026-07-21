from PySide6.QtGui import (
    QRadialGradient,
    QColor
)



class Glow:


    def create(
        self,
        center,
        radius
    ):


        gradient = QRadialGradient(
            center,
            radius
        )


        gradient.setColorAt(
            0,
            QColor(
                0,
                255,
                255,
                180
            )
        )


        gradient.setColorAt(
            0.25,
            QColor(
                0,
                180,
                255,
                90
            )
        )


        gradient.setColorAt(
            0.6,
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


        return gradient