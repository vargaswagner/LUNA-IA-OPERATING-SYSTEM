from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4



@dataclass
class BaseEvent:

    event_id: str = field(
        default_factory=lambda: str(uuid4())
    )

    created_at: datetime = field(
        default_factory=datetime.now
    )


@dataclass
class SystemStartedEvent(BaseEvent):

    message: str = "LUNA started"



@dataclass
class SystemStoppedEvent(BaseEvent):

    message: str = "LUNA stopped"



@dataclass
class VoiceReceivedEvent(BaseEvent):

    text: str = ""



@dataclass
class IntentDetectedEvent(BaseEvent):

    intent: str = ""

    confidence: float = 0.0



@dataclass
class ToolExecutionRequestedEvent(BaseEvent):

    tool_name: str = ""

    parameters: dict = field(
        default_factory=dict
    )



@dataclass
class ToolExecutedEvent(BaseEvent):

    tool_name: str = ""

    result: dict = field(
        default_factory=dict
    )
    
@dataclass
class AudioCapturedEvent(BaseEvent):

    audio_data: object = None

    sample_rate: int = 16000
    
@dataclass
class AudioFrameEvent(BaseEvent):

    audio_data: object = None

    sample_rate: int = 16000
    
    
@dataclass
class VoiceDetectedEvent(BaseEvent):

    audio_data: object = None

@dataclass
class WakeWordDetectedEvent(BaseEvent):

    word: str = "jarvis"

    confidence: float = 0.0


@dataclass
class SpeechRecognizedEvent(BaseEvent):

    text: str = ""

    language: str = "es"
    

@dataclass
class CompleteAudioEvent(BaseEvent):

    audio_data: object = None

    duration: float = 0.0
    

@dataclass
class CompleteAudioEvent(BaseEvent):

    audio_data: object = None

    sample_rate: int = 16000

    duration: float = 0.0