import math
import time


from PySide6.QtGui import (
    QColor,
    QPen
)


from PySide6.QtCore import Qt



class VoiceWave:


    def draw(
        self,
        painter,
        center
    ):


        t=time.time()



        painter.setBrush(
            Qt.NoBrush
        )


        for i in range(12):


            wave=math.sin(
                t*6+i
            )


            size=(
                80
                +
                i*8
                +
                wave*10
            )



            painter.setPen(

                QPen(

                    QColor(

                        0,

                        255,

                        255,

                        100-i*5

                    ),

                    1

                )

            )


            painter.drawEllipse(

                center,

                int(size),

                int(size)

            )