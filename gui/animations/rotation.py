import time



class Rotation:


    def __init__(
        self,
        speed=25
    ):

        self.speed=speed



    def angle(self):

        t=time.time()


        return (
            t*self.speed
        )%360



    def reverse_angle(self):

        return (
            360-
            self.angle()
        )