from loguru import logger



async def complete_audio_handler(event):

    logger.info(
        "Complete audio received"
    )


    logger.info(
        f"Frames: {len(event.audio_data)}"
    )