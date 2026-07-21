import random


from PySide6.QtGui import QColor



class ParticlesField:


    def __init__(self):

        self.particles=[]


        for i in range(150):

            self.particles.append(

                (

                random.randint(
                    0,
                    900
                ),

                random.randint(
                    0,
                    700
                )

                )

            )



    def draw(
        self,
        painter
    ):


        painter.setPen(

            QColor(
                0,
                200,
                255,
                150
            )

        )


        for x,y in self.particles:


            painter.drawPoint(
                x,
                y
            )