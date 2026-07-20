from loguru import logger

from app.dependency_container import container

from config.logging import setup_logging



async def startup():


    setup_logging()


    logger.info(
        "[BOOT] Loading Kernel"
    )


    logger.info(
        "[BOOT] Starting Event Bus"
    )


    logger.info(
        "[BOOT] Loading Plugins"
    )


    container.plugins.load_plugins()


    logger.info(
        "[BOOT] Loading Services"
    )


    await container.services.start_all()


    logger.info(
        "[BOOT] LUNA ONLINE"
    )