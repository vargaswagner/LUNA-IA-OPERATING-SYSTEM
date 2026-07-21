import random
import math



class Particle:


    def __init__(
        self,
        width,
        height
    ):

        self.reset(
            width,
            height
        )



    def reset(
        self,
        width,
        height
    ):

        self.x=random.randint(
            0,
            width
        )

        self.y=random.randint(
            0,
            height
        )


        self.z=random.random()


        self.speed=(
            0.2+
            self.z*1.5
        )


        self.size=(
            1+
            self.z*3
        )



    def update(
        self,
        height
    ):

        self.y-=self.speed


        if self.y<0:

            self.y=height



class Particles:


    def __init__(self):

        self.items=[
            Particle(
                900,
                700
            )
            for _ in range(300)
        ]



    def draw(
        self,
        canvas
    ):

        from PySide6.QtGui import (
            QPainter,
            QColor
        )


        painter=QPainter(canvas)


        for p in self.items:


            p.update(
                canvas.height()
            )


            alpha=int(
                80+
                p.z*150
            )


            painter.setBrush(
                QColor(
                    0,
                    220,
                    255,
                    alpha
                )
            )


            painter.drawEllipse(
                int(p.x),
                int(p.y),
                int(p.size),
                int(p.size)
            )


        painter.end()