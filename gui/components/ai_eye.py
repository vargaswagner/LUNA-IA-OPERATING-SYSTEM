import math
import time
import random


from PySide6.QtGui import (
    QColor,
    QPen,
    QBrush,
    QRadialGradient
)

from PySide6.QtCore import Qt



class AIEye:


    def __init__(self):

        self.start = time.time()


        self.particles=[]


        for i in range(40):

            self.particles.append({

                "angle":
                    random.random()*math.pi*2,

                "radius":
                    random.randint(
                        55,
                        120
                    ),

                "speed":
                    random.uniform(
                        .5,
                        2
                    )

            })




    def draw(
        self,
        painter,
        center
    ):


        t=time.time()-self.start



        #
        # RESPIRACION IA
        #

        breathe=(

            math.sin(
                t*3
            )

            +1

        )/2



        scale = (

            1

            +

            breathe*.15

        )



        #
        # CAMPO ENERGETICO
        #

        gradient = QRadialGradient(

            center,

            120*scale

        )


        gradient.setColorAt(

            0,

            QColor(
                255,
                255,
                255,
                220
            )

        )


        gradient.setColorAt(

            .2,

            QColor(
                0,
                255,
                255,
                200
            )

        )


        gradient.setColorAt(

            .5,

            QColor(
                0,
                120,
                255,
                80
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

            QBrush(
                gradient
            )

        )


        painter.setPen(
            Qt.NoPen
        )


        painter.drawEllipse(

            center,

            int(120*scale),

            int(120*scale)

        )



        #
        # LENTE HEXAGONAL
        #

        painter.setBrush(
            Qt.NoBrush
        )


        painter.setPen(

            QPen(

                QColor(
                    0,
                    240,
                    255,
                    180
                ),

                2

            )

        )



        points=[]


        for i in range(6):


            angle=(

                math.pi/3*i

                +

                t*.4

            )


            x=(

                center.x()

                +

                math.cos(angle)

                *

                65

            )


            y=(

                center.y()

                +

                math.sin(angle)

                *

                65

            )


            points.append((x,y))



        for i in range(6):


            x1,y1=points[i]

            x2,y2=points[(i+1)%6]


            painter.drawLine(

                int(x1),

                int(y1),

                int(x2),

                int(y2)

            )



        #
        # IRIS ROTATORIO
        #

        for r in (
            45,
            35,
            25
        ):


            painter.setPen(

                QPen(

                    QColor(

                        0,

                        255,

                        255,

                        140

                    ),

                    1

                )

            )


            painter.drawEllipse(

                center,

                r,

                r

            )



        #
        # NUCLEO
        #

        painter.setBrush(

            QColor(
                255,
                255,
                255
            )

        )


        painter.setPen(
            Qt.NoPen
        )


        painter.drawEllipse(

            center,

            12,

            12

        )



        #
        # PUPILA DIGITAL
        #

        offset = math.sin(
            t*2
        )*8



        painter.setBrush(

            QColor(
                0,
                40,
                80
            )

        )


        painter.drawEllipse(

            int(center.x()+offset),

            center.y()-5,

            10,

            10

        )



        #
        # PARTICULAS SENSOR
        #

        for p in self.particles:


            angle=(

                p["angle"]

                +

                t*p["speed"]

            )


            radius=p["radius"]



            x=(

                center.x()

                +

                math.cos(angle)

                *

                radius

            )


            y=(

                center.y()

                +

                math.sin(angle)

                *

                radius

            )


            painter.setBrush(

                QColor(

                    0,

                    255,

                    255,

                    180

                )

            )


            painter.drawEllipse(

                int(x),

                int(y),

                3,

                3

            )



        #
        # SCANNER
        #

        scan=(

            math.sin(
                t*4
            )

            *

            60

        )



        painter.setPen(

            QPen(

                QColor(
                    255,
                    255,
                    255,
                    120
                ),

                1

            )

        )


       