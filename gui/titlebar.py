from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout
)

from PySide6.QtCore import Qt



class TitleBar(QWidget):


    def __init__(self,parent):

        super().__init__()


        self.parent = parent


        self.setFixedHeight(
            35
        )


        layout = QHBoxLayout(
            self
        )


        layout.setContentsMargins(
            10,
            0,
            10,
            0
        )


        layout.addStretch()



        self.minimize = QPushButton(
            "—"
        )


        self.maximize = QPushButton(
            "□"
        )


        self.close = QPushButton(
            "×"
        )


        layout.addWidget(
            self.minimize
        )


        layout.addWidget(
            self.maximize
        )


        layout.addWidget(
            self.close
        )


        self.minimize.clicked.connect(
            self.parent.showMinimized
        )


        self.maximize.clicked.connect(
            self.toggle_maximize
        )


        self.close.clicked.connect(
            self.parent.close
        )


        self.start = None



    def toggle_maximize(self):

        if self.parent.isMaximized():

            self.parent.showNormal()

        else:

            self.parent.showMaximized()



    def mousePressEvent(self,event):

        if event.button()==Qt.LeftButton:

            self.start = (
                event.globalPosition()
                .toPoint()
            )



    def mouseMoveEvent(self,event):

        if self.start:

            delta = (
                event.globalPosition()
                .toPoint()
                -
                self.start
            )


            self.parent.move(
                self.parent.pos()
                +
                delta
            )


            self.start = (
                event.globalPosition()
                .toPoint()
            )