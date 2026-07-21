from PySide6.QtGui import (
    QPainter,
    QColor
)



class Painter:


    def clear(self,canvas):

        painter = QPainter(canvas)


        painter.fillRect(
            canvas.rect(),
            QColor(
                0,
                0,
                10,
                255
            )
        )


        painter.end()