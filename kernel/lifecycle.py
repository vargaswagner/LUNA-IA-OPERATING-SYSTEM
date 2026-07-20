from enum import Enum



class SystemState(Enum):

    STARTING="starting"

    RUNNING="running"

    STOPPING="stopping"

    STOPPED="stopped"



class Lifecycle:


    def __init__(self):

        self.state = SystemState.STOPPED



    def start(self):

        self.state = SystemState.STARTING



    def running(self):

        self.state = SystemState.RUNNING



    def stop(self):

        self.state = SystemState.STOPPING