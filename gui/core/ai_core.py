from PySide6.QtGui import QPainter


from gui.components.energy_core import EnergyCore
from gui.components.neural_network import NeuralNetwork
from gui.components.voice_wave import VoiceWave
from gui.components.data_streams import DataStreams
from gui.components.hologram_grid import HologramGrid
from gui.components.particles_field import ParticlesField
from gui.components.ai_eye import AIEye
from gui.components.status_hud import StatusHUD



class AICore:


    def __init__(self):


        # núcleo energético

        self.energy = EnergyCore()



        # conexiones neuronales

        self.neural = NeuralNetwork()



        # voz IA

        self.voice = VoiceWave()



        # información flotante

        self.streams = DataStreams()



        # espacio holográfico

        self.grid = HologramGrid()



        # partículas

        self.particles = ParticlesField()



        # ojo IA

        self.eye = AIEye()



        # HUD

        self.status = StatusHUD()




    def draw(
        self,
        canvas
    ):


        painter = QPainter(
            canvas
        )


        try:


            painter.setRenderHint(
                QPainter.RenderHint.Antialiasing,
                True
            )


            center = (
                canvas.rect()
                .center()
            )



            #
            # CAPA ESPACIAL
            #

            self.particles.draw(
                painter
            )



            self.grid.draw(
                painter,
                canvas
            )



            #
            # SISTEMA IA
            #

            self.streams.draw(
                painter,
                canvas
            )



            self.neural.draw(
                painter,
                center
            )



            #
            # INTERFAZ DE VOZ
            #

            self.voice.draw(
                painter,
                center
            )



            #
            # NUCLEO PRINCIPAL
            #

            self.energy.draw(
                painter,
                center
            )



            #
            # CONCIENCIA IA
            #

            self.eye.draw(
                painter,
                center
            )



            #
            # INFORMACION
            #

            self.status.draw(
                painter
            )



        finally:


            painter.end()