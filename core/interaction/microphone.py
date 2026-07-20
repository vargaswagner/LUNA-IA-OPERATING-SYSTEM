import sounddevice as sd

from loguru import logger

from core.base_service import BaseService

from events.events import AudioCapturedEvent


class MicrophoneService(BaseService):


    def __init__(self, event_bus, dispatcher, audio_buffer):

        super().__init__(
            "MicrophoneService"
        )

        self.event_bus = event_bus

        self.dispatcher = dispatcher
        
        self.buffer = audio_buffer
        
        self.stream = None
        
        self.running = False


    async def start(self):

        logger.info(
            "Microphone service started"
        )

        self.running = True


        stream = sd.InputStream(
            samplerate=16000,
            channels=1,
            callback=self.audio_callback
        )


        stream.start()



    def audio_callback(
        self,
        indata,
        frames,
        time,
        status
    ):

        if status:
            logger.warning(status)


        audio = indata.copy()


        self.dispatcher.dispatch(
            self.buffer.handle_audio(audio)
        )

        # publicar evento
        # luego lo conectamos async correctamente



    async def stop(self):

        if self.stream:

            self.stream.stop()

            self.stream.close()


        logger.info(
            "Microphone stopped"
        )