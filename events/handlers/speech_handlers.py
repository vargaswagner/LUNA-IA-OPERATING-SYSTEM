from loguru import logger



async def speech_recognized_handler(event):

    logger.info(
        "================================"
    )


    logger.info(
        f"USER SAID: {event.text}"
    )


    logger.info(
        "================================"
    )