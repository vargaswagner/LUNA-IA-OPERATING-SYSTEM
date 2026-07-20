from loguru import logger


from app.dependency_container import container


from config.logging import setup_logging


from events.events import (
    SystemStartedEvent,
    WakeWordDetectedEvent,
    SpeechRecognizedEvent,
    AudioFrameEvent,
    CompleteAudioEvent,
)


from events.handlers.system_handlers import (
    system_started_handler,
)


from events.handlers.wakeword_handlers import (
    wakeword_detected_handler,
)


from events.handlers.speech_handlers import (
    speech_recognized_handler,
)


from events.handlers.audio_handlers import (
    complete_audio_handler,
)


from core.interaction.microphone import (
    MicrophoneService,
)


from core.interaction.hotword import (
    HotwordService,
)


from core.interaction.speaker import (
    SpeakerService,
)


from core.perception.audio_processor import (
    AudioProcessorService,
)


from core.perception.voice_activity import (
    VoiceActivityDetector,
)


from core.perception.audio_buffer import (
    AudioBufferService,
)


from core.perception.silence_detector import (
    SilenceDetectorService,
)


from core.perception.speech_to_text import (
    SpeechToTextService,
)



# ======================================================
# MAIN STARTUP
# ======================================================


async def startup():

    setup_logging()


    logger.info(
        "[BOOT] Loading Kernel"
    )


    register_events()


    load_plugins()


    register_services()


    logger.info(
        "[BOOT] Starting Services"
    )


    await container.services.start_all()



    await container.event_bus.publish(
        SystemStartedEvent()
    )


    logger.info(
        "[BOOT] JARVIS ONLINE"
    )



# ======================================================
# EVENT BUS REGISTRATION
# ======================================================


def register_events():

    logger.info(
        "[BOOT] Registering Events"
    )


    subscriptions = [

        (
            SystemStartedEvent,
            system_started_handler
        ),


        (
            WakeWordDetectedEvent,
            wakeword_detected_handler
        ),


        (
            SpeechRecognizedEvent,
            speech_recognized_handler
        ),


        (
            CompleteAudioEvent,
            complete_audio_handler
        ),

    ]


    for event, handler in subscriptions:

        container.event_bus.subscribe(
            event,
            handler
        )



# ======================================================
# PLUGINS
# ======================================================


def load_plugins():

    logger.info(
        "[BOOT] Loading Plugins"
    )


    container.plugins.load_plugins()



# ======================================================
# SERVICES
# ======================================================


def register_services():

    logger.info(
        "[BOOT] Registering Services"
    )


    audio_buffer = AudioBufferService(
        container.event_bus
    )


    speech_to_text = SpeechToTextService(
        container.event_bus
    )



    services = {


        "microphone":
            MicrophoneService(
                container.event_bus,
                container.dispatcher,
                audio_buffer
            ),


        "hotword":
            HotwordService(
                container.event_bus
            ),


        "speaker":
            SpeakerService(
                container.event_bus
            ),


        "audio_processor":
            AudioProcessorService(
                container.event_bus
            ),


        "voice_activity":
            VoiceActivityDetector(
                container.event_bus
            ),


        "audio_buffer":
            audio_buffer,


        "silence_detector":
            SilenceDetectorService(
                container.event_bus,
                audio_buffer
            ),


        "speech_to_text":
            speech_to_text,

    }



    for name, service in services.items():

        container.services.register(
            name,
            service
        )



    register_audio_pipeline(
        audio_buffer,
        speech_to_text
    )



# ======================================================
# AUDIO EVENT PIPELINE
# ======================================================


def register_audio_pipeline(
    audio_buffer,
    speech_to_text
):


    container.event_bus.subscribe(

        AudioFrameEvent,

        audio_buffer.handle_audio

    )


    container.event_bus.subscribe(

        CompleteAudioEvent,

        speech_to_text.transcribe

    )