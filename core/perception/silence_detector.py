from loguru import logger

from core.base_service import BaseService



class SilenceDetectorService(BaseService):


    def __init__(
        self,
        event_bus,
        buffer
    ):

        super().__init__(
            "SilenceDetector"
        )

        self.event_bus = event_bus

        self.buffer = buffer



    async def silence_detected(self):

        logger.info(
            "Speech ended"
        )


        await self.buffer.flush()



    async def start(self):

        logger.info(
            "Silence detector started"
        )



    async def stop(self):

        logger.info(
            "Silence detector stopped"
        )