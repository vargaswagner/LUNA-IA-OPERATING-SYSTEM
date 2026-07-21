from PySide6.QtGui import (
    QPainter,
    QRadialGradient,
    QColor
)



class Universe:


    def draw(self,canvas):

        painter = QPainter(canvas)


        gradient = QRadialGradient(
            canvas.rect().center(),
            500
        )


        gradient.setColorAt(
            0,
            QColor(
                0,
                40,
                100,
                180
            )
        )


        gradient.setColorAt(
            1,
            QColor(
                0,
                0,
                20,
                255
            )
        )


        painter.fillRect(
            canvas.rect(),
            gradient
        )


        painter.end()