from loguru import logger

from core.base_service import BaseService

from events.events import AudioFrameEvent



class AudioProcessorService(BaseService):


    def __init__(
        self,
        event_bus
    ):

        super().__init__(
            "AudioProcessorService"
        )

        self.event_bus = event_bus



    async def start(self):

        logger.info(
            "Audio processor started"
        )



    async def stop(self):

        logger.info(
            "Audio processor stopped"
        )