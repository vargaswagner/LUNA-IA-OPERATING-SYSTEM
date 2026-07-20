from collections import defaultdict
from typing import Callable


class EventBus:


    def __init__(self):

        self.listeners = defaultdict(list)



    def subscribe(
        self,
        event_name: str,
        callback: Callable
    ):

        self.listeners[event_name].append(callback)



    async def publish(
        self,
        event
    ):

        listeners = self.listeners.get(
            event.name,
            []
        )


        for listener in listeners:

            await listener(event)