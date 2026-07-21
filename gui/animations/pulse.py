import math
import time


class Pulse:


    def __init__(
        self,
        speed=2.2,
        smoothness=0.7
    ):

        self.speed = speed
        self.smoothness = smoothness



    def value(self):

        t = time.time()


        wave = (
            math.sin(
                t * self.speed
            )
            +
            math.sin(
                t * self.speed * 0.43
            )
            *
            0.25
        )


        return (
            wave + 1.25
        ) / 2.25



    def radius(
        self,
        base,
        intensity
    ):

        return (
            base
            +
            self.value()
            *
            intensity
        )