class Registry:


    def __init__(self):

        self.items = {}



    def register(
        self,
        key,
        value
    ):

        self.items[key] = value



    def get(
        self,
        key
    ):

        return self.items.get(key)



registry = Registry()