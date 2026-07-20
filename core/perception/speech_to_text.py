from loguru import logger

from faster_whisper import WhisperModel

from core.base_service import BaseService

from config.ai import (
    WHISPER_MODEL,
    WHISPER_DEVICE,
    WHISPER_COMPUTE
)

from events.events import (
    SpeechRecognizedEvent
)



class SpeechToTextService(BaseService):


    def __init__(
        self,
        event_bus
    ):

        super().__init__(
            "SpeechToTextService"
        )

        self.event_bus = event_bus

        self.model = None



    async def start(self):

        logger.info(
            "Loading Whisper..."
        )

        logger.info(
            f"MODEL: {WHISPER_MODEL}"
        )

        logger.info(
            f"DEVICE: {WHISPER_DEVICE}"
        )

        logger.info(
            f"COMPUTE: {WHISPER_COMPUTE}"
        )


        # self.model = WhisperModel(
        #     WHISPER_MODEL,
        #     device=WHISPER_DEVICE,
        #     compute_type=WHISPER_COMPUTE
        # )

        logger.info(
            "Whisper ready"
        )

        input("ESPERANDO...")

    async def stop(self):

        logger.info(
            "Speech recognition stopped"
        )

        self.model = None


    async def transcribe(
        self,
        event
    ):


        segments, info = self.model.transcribe(
            event.audio_data,
            language="es"
        )


        text = ""


        for segment in segments:

            text += segment.text



        text = text.strip()



        if text:


            await self.event_bus.publish(
                SpeechRecognizedEvent(
                    text=text,
                    language="es"
                )
            )
    
    