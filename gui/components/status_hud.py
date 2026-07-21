from PySide6.QtGui import QColor,QFont



class StatusHUD:


    def draw(
        self,
        painter
    ):


        painter.setFont(

            QFont(
                "Consolas",
                12
            )

        )


        painter.setPen(

            QColor(
                0,
                255,
                255
            )

        )


        painter.drawText(

            30,

            650,

            "JARVIS ONLINE | LISTENING"

        )