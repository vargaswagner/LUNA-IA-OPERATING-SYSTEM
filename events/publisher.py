from events.bus import EventBus



class EventPublisher:


    def __init__(
        self,
        bus: EventBus
    ):

        self.bus = bus



    async def publish(
        self,
        event
    ):

        await self.bus.publish(
            event
        )