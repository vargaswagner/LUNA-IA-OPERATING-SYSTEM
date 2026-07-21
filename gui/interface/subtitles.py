from PySide6.QtGui import (
    QPainter,
    QColor,
    QFont
)



class Subtitles:


    def __init__(self):

        self.text = ""



    def update(
        self,
        text
    ):

        self.text=text



    def draw(
        self,
        canvas
    ):


        if not self.text:

            return



        painter = QPainter(canvas)



        painter.setPen(
            QColor(
                220,
                255,
                255
            )
        )


        painter.setFont(
            QFont(
                "Consolas",
                14
            )
        )



        painter.drawText(
            canvas.width()//2-150,
            canvas.height()-80,
            self.text
        )


        painter.end()