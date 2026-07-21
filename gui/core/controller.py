from gui.core.state import AIState



class AIController:


    def __init__(self):

        self.state = AIState.IDLE


        self.message = (
            "WAITING FOR INPUT"
        )



    def set_state(
        self,
        state,
        message=None
    ):


        self.state = state


        if message:

            self.message = message



controller = AIController()