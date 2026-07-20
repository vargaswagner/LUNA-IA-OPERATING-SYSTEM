import asyncio

from events.dispatcher import EventDispatcher

from app.dependency_container import container

from app.startup import startup
from app.shutdown import shutdown

from loguru import logger



async def run():

    loop = asyncio.get_running_loop()


    container.dispatcher = EventDispatcher(
        loop
    )


    try:

        await startup()


        logger.info(
            "Kernel running..."
        )


        while True:

            await asyncio.sleep(1)



    except asyncio.CancelledError:

        logger.info(
            "Main task cancelled"
        )



    except Exception:

        logger.exception(
            "Fatal error in JARVIS"
        )



    finally:

        await shutdown()