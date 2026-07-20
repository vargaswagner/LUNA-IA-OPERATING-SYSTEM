from loguru import logger

from core.base_service import BaseService

from events.events import (
    AudioFrameEvent,
    CompleteAudioEvent
)



class AudioBufferService(BaseService):


    def __init__(
        self,
        event_bus
    ):

        super().__init__(
            "AudioBufferService"
        )

        self.event_bus = event_bus

        self.buffer = []



    async def handle_audio(
        self,
        event: AudioFrameEvent
    ):

        self.buffer.append(
            event.audio_data
        )


        logger.debug(
            "Audio frame stored"
        )



    async def flush(self):

        if not self.buffer:
            return


        complete_event = CompleteAudioEvent(
            audio_data=self.buffer
        )


        self.buffer = []


        await self.event_bus.publish(
            complete_event
        )



    async def start(self):

        logger.info(
            "Audio buffer started"
        )



    async def stop(self):

        logger.info(
            "Audio buffer stopped"
        )