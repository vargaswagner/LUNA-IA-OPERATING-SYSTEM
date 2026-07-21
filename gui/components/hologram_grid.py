import math
import random
import time


from PySide6.QtGui import (
    QColor,
    QPen,
    QBrush
)

from PySide6.QtCore import Qt



class HologramGrid:


    def __init__(self):

        self.nodes=[]


        for i in range(80):

            self.nodes.append({

                "angle":
                    random.uniform(
                        0,
                        math.pi*2
                    ),


                "radius":
                    random.randint(
                        120,
                        320
                    ),


                "speed":
                    random.uniform(
                        0.2,
                        1.5
                    ),


                "size":
                    random.randint(
                        1,
                        4
                    )

            })



    def draw(
        self,
        painter,
        center
    ):


        t=time.time()



        #
        # PARTICULAS CUANTICAS
        #

        for node in self.nodes:


            angle = (

                node["angle"]

                +

                t *
                node["speed"]

            )


            pulse = (

                math.sin(
                    t*3+
                    node["radius"]
                )

                +1

            ) /2



            radius = (

                node["radius"]

                +

                pulse*20

            )



            x = (

                center.x()

                +

                math.cos(angle)

                *

                radius

            )


            y = (

                center.y()

                +

                math.sin(angle)

                *

                radius

            )



            alpha = int(

                80

                +

                pulse*150

            )


            painter.setPen(
                Qt.NoPen
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

                int(x),

                int(y),

                node["size"],

                node["size"]

            )



        #
        # CONEXIONES INTELIGENTES
        #

        painter.setPen(

            QPen(

                QColor(

                    0,

                    180,

                    255,

                    25

                ),

                1

            )

        )


        active=[]


        for node in self.nodes:


            angle=(

                node["angle"]

                +

                t *
                node["speed"]

            )


            radius=node["radius"]



            active.append(

                (

                    center.x()
                    +
                    math.cos(angle)
                    *
                    radius,


                    center.y()
                    +
                    math.sin(angle)
                    *
                    radius

                )

            )



        for i in range(
            0,
            len(active),
            3
        ):


            x1,y1=active[i]


            for j in range(
                i+1,
                min(
                    i+5,
                    len(active)
                )
            ):


                x2,y2=active[j]


                distance=math.sqrt(

                    (x2-x1)**2
                    +
                    (y2-y1)**2

                )



                if distance < 90:


                    painter.drawLine(

                        int(x1),
                        int(y1),

                        int(x2),
                        int(y2)

                    )