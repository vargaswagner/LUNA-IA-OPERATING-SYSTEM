from PySide6.QtGui import (
    QPainter,
    QColor,
    QFont
)



class Status:


    def draw(self,canvas):

        painter = QPainter(canvas)


        painter.setPen(
            QColor(
                0,
                230,
                255
            )
        )


        painter.setFont(
            QFont(
                "Consolas",
                16
            )
        )


        painter.drawText(
            40,
            50,
            "J.A.R.V.I.S"
        )


        painter.drawText(
            40,
            80,
            "COGNITIVE CORE ACTIVE"
        )


        painter.end()