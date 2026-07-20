from events.bus import EventBus



class EventSubscriber:


    def __init__(
        self,
        bus: EventBus
    ):

        self.bus = bus



    def subscribe(
        self,
        event_type,
        handler
    ):

        self.bus.subscribe(
            event_type,
            handler
        )