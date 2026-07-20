from loguru import logger

from core.base_service import BaseService



class SpeakerService(BaseService):


    def __init__(
        self,
        event_bus
    ):

        super().__init__(
            "SpeakerService"
        )

        self.event_bus = event_bus



    async def speak(
        self,
        text:str
    ):

        logger.info(
            f"JARVIS: {text}"
        )



    async def start(self):

        logger.info(
            "Speaker ready"
        )



    async def stop(self):

        logger.info(
            "Speaker stopped"
        )