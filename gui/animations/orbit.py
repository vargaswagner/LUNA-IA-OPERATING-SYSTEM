import math



class Orbit:


    def generate(
        self,
        center,
        radius,
        rotation,
        tilt=0
    ):


        points=[]


        for i in range(180):


            angle=(
                math.pi*2*i/180
            )


            x=(
                math.cos(angle)
                *
                radius
            )


            y=(
                math.sin(angle)
                *
                radius
                *
                math.cos(
                    math.radians(
                        tilt
                    )
                )
            )


            rot=math.radians(
                rotation
            )


            rx=(
                x*math.cos(rot)
                -
                y*math.sin(rot)
            )


            ry=(
                x*math.sin(rot)
                +
                y*math.cos(rot)
            )


            points.append(
                (
                    center.x()+rx,
                    center.y()+ry
                )
            )


        return points