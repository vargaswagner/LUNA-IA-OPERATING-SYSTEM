from loguru import logger


async def shutdown():

    logger.info(
        "Stopping LUNA..."
    )

    logger.info(
        "LUNA stopped"
    )