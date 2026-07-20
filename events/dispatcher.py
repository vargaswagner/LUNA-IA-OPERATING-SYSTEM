import asyncio

from loguru import logger

class EventDispatcher:


    def __init__(
        self,
        loop
    ):

        self.loop = loop



    def dispatch(
        self,
        coroutine
    ):
        if self.loop.is_closed():

            logger.warning(
                "Event loop closed, ignoring event"
            )

            return


        asyncio.run_coroutine_threadsafe(
            coroutine,
            self.loop
        )