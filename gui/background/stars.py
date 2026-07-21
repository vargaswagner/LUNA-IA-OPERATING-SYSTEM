from PySide6.QtGui import (
    QPainter,
    QColor
)

import random



class Star:


    def __init__(self):

        self.x=random.randint(0,900)
        self.y=random.randint(0,700)

        self.speed=random.uniform(
            0.1,
            0.8
        )



    def update(self):

        self.y += self.speed

        if self.y > 700:
            self.y = 0



class Stars:


    def __init__(self):

        self.stars=[
            Star()
            for _ in range(200)
        ]



    def draw(self,canvas):

        painter = QPainter(canvas)


        for star in self.stars:

            star.update()


            painter.setBrush(
                QColor(
                    180,
                    230,
                    255
                )
            )


            painter.drawEllipse(
                star.x,
                star.y,
                2,
                2
            )


        painter.end()