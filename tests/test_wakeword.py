import pytest

from events.events import (
    WakeWordDetectedEvent
)



@pytest.mark.asyncio
async def test_wakeword():

    event = WakeWordDetectedEvent(
        word="jarvis",
        confidence=0.98
    )


    assert event.word == "jarvis"

    assert event.confidence > 0.9