import random
import math
import time


from PySide6.QtGui import (
    QColor,
    QPen,
    QBrush
)

from PySide6.QtCore import Qt



class NeuralNetwork:


    def __init__(self):

        self.nodes=[]


        for i in range(70):

            self.nodes.append({

                "angle":
                    random.uniform(
                        0,
                        math.pi*2
                    ),


                "radius":
                    random.randint(
                        100,
                        260
                    ),


                "speed":
                    random.uniform(
                        0.2,
                        1.2
                    ),


                "size":
                    random.randint(
                        2,
                        5
                    ),


                "pulse":
                    random.random()*10

            })



    def draw(
        self,
        painter,
        center
    ):


        t=time.time()



        positions=[]



        #
        # CALCULAR NODOS
        #

        for node in self.nodes:


            angle=(

                node["angle"]

                +

                t*node["speed"]

            )


            breathing=(

                math.sin(

                    t*3

                    +

                    node["pulse"]

                )

                +1

            )/2



            radius=(

                node["radius"]

                +

                breathing*15

            )



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


            positions.append(

                (
                    x,
                    y,
                    breathing,
                    node["size"]

                )

            )



        #
        # CONEXIONES NEURONALES
        #

        for i in range(

            len(positions)

        ):


            x1,y1,_,_=positions[i]



            for j in range(

                i+1,

                len(positions)

            ):


                x2,y2,_,_=positions[j]



                distance=math.sqrt(

                    (x2-x1)**2

                    +

                    (y2-y1)**2

                )



                if distance < 90:



                    alpha=int(

                        100

                        -

                        distance

                    )



                    painter.setPen(

                        QPen(

                            QColor(

                                0,

                                180,

                                255,

                                max(

                                    alpha,

                                    15

                                )

                            ),

                            1

                        )

                    )



                    painter.drawLine(

                        int(x1),

                        int(y1),

                        int(x2),

                        int(y2)

                    )



        #
        # NODOS IA
        #

        painter.setPen(
            Qt.NoPen
        )



        for x,y,pulse,size in positions:



            glow=int(

                100

                +

                pulse*155

            )



            painter.setBrush(

                QColor(

                    0,

                    240,

                    255,

                    glow

                )

            )



            painter.drawEllipse(

                int(x-size),

                int(y-size),

                int(size*2),

                int(size*2)

            )



        #
        # PULSOS DE INFORMACION
        #

        painter.setPen(

            QPen(

                QColor(

                    255,

                    255,

                    255,

                    180

                ),

                2

            )

        )



        for i in range(
            8
        ):


            index=random.randint(

                0,

                len(positions)-1

            )


            x,y,_,_=positions[index]



            painter.drawPoint(

                int(x),

                int(y)

            )