class AlphaMux:
    alpha_code = 'abcdefghijklmnopqrstuvwxyz*'

    def __init__(self, cls):
        assert isinstance(cls, type), "Wrong Usage!"
        self.__container = {k: cls() for k in self.alpha_code}

    def mux(self, key: str):
        return self.__container[key[0].lower()] if key[0].isalpha() else self.__container['*']
