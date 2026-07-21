import math
import random
import time


from PySide6.QtGui import (
    QColor,
    QFont,
    QPen
)


from PySide6.QtCore import Qt



class DataStreams:


    def __init__(self):

        self.start=time.time()


        self.lines=[

            "NEURAL CORE",

            "VOICE ENGINE",

            "MEMORY MATRIX",

            "VISION SYSTEM",

            "QUANTUM PROCESS",

            "AI NETWORK"

        ]



        self.values={

            item:
            random.randint(
                40,
                99
            )

            for item in self.lines

        }



    def draw(
        self,
        painter,
        canvas
    ):


        t=time.time()-self.start



        #
        # FUENTE FUTURISTA
        #

        painter.setFont(

            QFont(

                "Consolas",

                10

            )

        )



        x=30

        y=60


        #
        # TITULO
        #

        painter.setPen(

            QColor(

                0,

                255,

                255,

                220

            )

        )


        painter.drawText(

            x,

            y-25,

            "JARVIS // DATA STREAM"

        )



        #
        # DATOS DINAMICOS
        #

        for i,name in enumerate(
            self.lines
        ):



            #
            # actualizar valores
            #

            value=(

                self.values[name]

                +

                random.uniform(
                    -1,
                    1
                )

            )



            self.values[name]=value



            alpha=int(

                120

                +

                abs(
                    math.sin(t+i)
                )

                *

                100

            )



            painter.setPen(

                QColor(

                    0,

                    220,

                    255,

                    alpha

                )

            )



            text=(

                f"{name:<16}"

                +

                f"{value:05.1f}%"

            )



            painter.drawText(

                x,

                y+i*28,

                text

            )



        #
        # DATA PACKETS
        #

        painter.setPen(

            QColor(

                0,

                255,

                180,

                160

            )

        )


        packet=""

        for i in range(18):


            packet += random.choice(

                "01"

            )



        painter.drawText(

            30,

            245,

            "PACKET: "+packet

        )