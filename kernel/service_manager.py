from loguru import logger


class ServiceManager:


    def __init__(self):

        self.services = {}



    def register(
        self,
        name: str,
        service
    ):

        self.services[name] = service

        logger.info(
            f"Service registered: {name}"
        )



    async def start_all(self):

        logger.info(
            "Starting services..."
        )


        for name, service in self.services.items():

            if hasattr(service, "start"):

                await service.start()

                logger.info(
                    f"Started service: {name}"
                )



    async def stop_all(self):

        logger.info(
            "Stopping services..."
        )


        for name, service in self.services.items():

            if hasattr(service, "stop"):

                await service.stop()