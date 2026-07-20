from loguru import logger



async def wakeword_detected_handler(event):

    logger.info(
        f"Wake word detected: {event.word}"
    )

    logger.info(
        f"Confidence: {event.confidence}"
    )