from loguru import logger

from core.base_service import BaseService

from events.events import WakeWordDetectedEvent



class HotwordService(BaseService):


    def __init__(
        self,
        event_bus
    ):

        super().__init__(
            "HotwordService"
        )

        self.event_bus = event_bus



    async def start(self):

        logger.info(
            "Wake word engine started"
        )



    async def stop(self):

        logger.info(
            "Wake word engine stopped"
        )

