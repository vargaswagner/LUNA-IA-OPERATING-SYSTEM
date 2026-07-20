from loguru import logger


class PluginManager:


    def __init__(self):

        self.plugins = []



    def load_plugins(self):

        logger.info(
            "Loading plugins..."
        )


        # futuro:
        # buscar carpetas automáticamente



    def register(self, plugin):

        self.plugins.append(plugin)