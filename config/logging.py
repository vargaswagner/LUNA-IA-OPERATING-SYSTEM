from loguru import logger
import sys


def setup_logging():

    logger.remove()

    logger.add(
        sys.stdout,
        level="INFO"
    )

    logger.add(
        "logs/luna.log",
        rotation="10 MB",
        retention="10 days"
    )

    logger.info(
        "Logging initialized"
    )

