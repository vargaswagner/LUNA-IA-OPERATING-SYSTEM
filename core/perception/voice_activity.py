from loguru import logger

from core.base_service import BaseService



class VoiceActivityDetector(
    BaseService
):


    def __init__(
        self,
        event_bus
    ):

        super().__init__(
            "VoiceActivityDetector"
        )

        self.event_bus = event_bus



    async def start(self):

        logger.info(
            "VAD started"
        )



    async def stop(self):

        logger.info(
            "VAD stopped"
        )