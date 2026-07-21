import math
import time
import random

from PySide6.QtGui import (
    QPainter,
    QColor,
    QRadialGradient,
    QBrush
)


class Nebula:


    def __init__(self):

        self.start_time = time.time()


        self.clouds = []


        for i in range(6):

            self.clouds.append({

                "offset_x": random.randint(
                    -300,
                    300
                ),

                "offset_y": random.randint(
                    -250,
                    250
                ),

                "radius": random.randint(
                    180,
                    350
                ),

                "speed": random.uniform(
                    0.2,
                    0.5
                ),

                "phase": random.uniform(
                    0,
                    math.pi * 2
                ),

                "color": random.choice([

                    (
                        0,
                        180,
                        255
                    ),

                    (
                        120,
                        80,
                        255
                    ),

                    (
                        0,
                        255,
                        220
                    )

                ])

            })



    def draw(
        self,
        canvas
    ):


        painter = QPainter(
            canvas
        )


        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )


        center = (
            canvas.rect()
            .center()
        )


        t = (
            time.time()
            -
            self.start_time
        )


        for cloud in self.clouds:


            movement_x = math.sin(
                t *
                cloud["speed"]
                +
                cloud["phase"]
            ) * 80


            movement_y = math.cos(
                t *
                cloud["speed"]
                *0.8
                +
                cloud["phase"]
            ) * 60



            pulse = (
                math.sin(
                    t*1.5
                    +
                    cloud["phase"]
                )
                +
                1
            ) / 2



            radius = (
                cloud["radius"]
                +
                pulse*40
            )



            x = (
                center.x()
                +
                cloud["offset_x"]
                +
                movement_x
            )


            y = (
                center.y()
                +
                cloud["offset_y"]
                +
                movement_y
            )



            r,g,b = cloud["color"]



            gradient = QRadialGradient(

                x,
                y,
                radius

            )


            gradient.setColorAt(

                0,

                QColor(

                    r,
                    g,
                    b,
                    55
                )

            )


            gradient.setColorAt(

                0.35,

                QColor(

                    r,
                    g,
                    b,
                    25
                )

            )


            gradient.setColorAt(

                1,

                QColor(

                    r,
                    g,
                    b,
                    0
                )

            )



            painter.setBrush(
                QBrush(
                    gradient
                )
            )


            painter.setPen(
                QColor(
                    0,
                    0,
                    0,
                    0
                )
            )


            painter.drawEllipse(

                int(x-radius),

                int(y-radius),

                int(radius*2),

                int(radius*2)

            )


        painter.end()