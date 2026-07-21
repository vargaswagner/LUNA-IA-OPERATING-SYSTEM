import time

from PySide6.QtGui import (
    QPainter,
    QColor,
    QPen
)


class HolographicRings:


    def __init__(self):

        pass



    def draw(
        self,
        painter,
        center
    ):

        # painter = QPainter(canvas)

        # try:

        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing,
            True
        )


        painter.setPen(
            QPen(
                QColor(
                    0,
                    230,
                    255,
                    150
                ),
                2
            )
        )


        painter.drawEllipse(
            center,
            100,
            100
        )


        # finally:

            # painter.end()