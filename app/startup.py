from loguru import logger

from app.dependency_container import container

from config.logging import setup_logging

from events.events import SystemStartedEvent

from events.handlers.system_handlers import (
    system_started_handler
)

from app.dependency_container import container


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
    
    container.event_bus.subscribe(
        SystemStartedEvent,
        system_started_handler
    )


    await container.event_bus.publish(
        SystemStartedEvent()
    )


    await container.services.start_all()


    logger.info(
        "[BOOT] LUNA ONLINE"
    )