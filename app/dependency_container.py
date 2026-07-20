from events.bus import EventBus

from kernel.service_manager import ServiceManager

from kernel.plugin_manager import PluginManager

from kernel.registry import Registry



class Container:


    def __init__(self):

        self.event_bus = EventBus()

        self.services = ServiceManager()

        self.plugins = PluginManager()

        self.registry = Registry()

        self.dispatcher = None

container = Container()