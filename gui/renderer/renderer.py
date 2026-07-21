from gui.renderer.painter import Painter

from gui.background.universe import Universe
from gui.background.stars import Stars
from gui.background.nebula import Nebula

from gui.core.ai_core import AICore

from gui.effects.particles import Particles
from gui.effects.scan import Scan

from gui.interface.status import Status



class Renderer:


    def __init__(self):

        self.painter = Painter()

        self.universe = Universe()

        # self.stars = Stars()

        self.nebula = Nebula()
        
        # self.particles = Particles()

        self.core = AICore()

        # self.scan = Scan()

        # self.status = Status()



    def draw(self,canvas):


        self.painter.clear(
            canvas
        )


        self.universe.draw(
            canvas
        )


        self.nebula.draw(
            canvas
        )


        # self.stars.draw(
        #     canvas
        # )


        # self.particles.draw(
        #     canvas
        # )


        self.core.draw(
            canvas
        )


        # self.scan.draw(
        #     canvas
        # )


        # self.status.draw(
        #     canvas
        # )