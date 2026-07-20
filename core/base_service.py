from abc import ABC, abstractmethod



class BaseService(ABC):


    def __init__(self, name):

        self.name = name



    @abstractmethod
    async def start(self):

        pass



    @abstractmethod
    async def stop(self):

        pass