# import sys
# import asyncio

# from PySide6.QtWidgets import QApplication

# from qasync import QEventLoop

# from gui.window import JarvisWindow


# class JarvisApplication:

#     def __init__(self):

#         self.qt = QApplication(sys.argv)

#         self.loop = QEventLoop(self.qt)

#         asyncio.set_event_loop(self.loop)

#         self.window = JarvisWindow()

#     async def initialize(self):

#         """
#         Aquí luego iniciaremos:

#         - DependencyContainer
#         - EventBus
#         - Kernel
#         - Plugins
#         - IA
#         """

#         pass

#     def run(self):

#         self.window.show()

#         with self.loop:

#             self.loop.create_task(self.initialize())

#             self.loop.run_forever()


# def run():

#     JarvisApplication().run()


import sys

from PySide6.QtWidgets import QApplication

from gui.window import JarvisWindow



class JarvisApp:


    def __init__(self):

        print("Creando QApplication")

        self.app = QApplication(sys.argv)


        print("Creando ventana")

        self.window = JarvisWindow()



    def run(self):

        print("Mostrando ventana")

        self.window.show()


        print("Entrando al loop Qt")


        self.app.exec()


        print("Qt cerrado")