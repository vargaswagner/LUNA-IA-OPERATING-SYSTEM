from collections import defaultdict

from typing import Callable, Type

from loguru import logger



class EventBus:


    def __init__(self):

        self.listeners = defaultdict(list)



    def subscribe(
        self,
        event_type: Type,
        handler: Callable
    ):


        self.listeners[event_type].append(
            handler
        )


        logger.info(
            f"Subscribed: {event_type.__name__}"
        )



    async def publish(
        self,
        event
    ):


        event_type = type(event)


        handlers = self.listeners.get(
            event_type,
            []
        )


        logger.info(
            f"Publishing: {event_type.__name__}"
        )


        for handler in handlers:

            await handler(event)
