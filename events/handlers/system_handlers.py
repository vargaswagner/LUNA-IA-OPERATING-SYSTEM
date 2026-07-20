from loguru import logger



async def system_started_handler(event):

    logger.info(
        f"SYSTEM EVENT: {event.message}"
    )



async def system_stopped_handler(event):

    logger.info(
        f"SYSTEM EVENT: {event.message}"
    )