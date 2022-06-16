from common.ads.sll import SortedLinkedList
from common.metaclass.singleton import SingletonMetaclass
from common.mux import AlphaMux
from .db import DVDController


class DVListType(metaclass=SingletonMetaclass):
    def __init__(self):
        self.__mux = AlphaMux(SortedLinkedList)
        self.__db = DVDController()

        print('loading dvd data from db...')
        dvds = self.__db.fetch_all()
        for dvd in dvds:
            sll = self.mux(dvd.name)
            sll.add(dvd.name, dvd)
        else:
            print('loaded dvd data successfully!')

    def mux(self, name):
        return self.__mux.mux(name)

    def add(self, dvd):
        sll = self.mux(dvd.name)
        try:
            dvd.db_id = self.__db.add(
                dvd.name,
                dvd.stars,
                dvd.producer,
                dvd.director,
                dvd.production_company,
                dvd.total_quantity
            )
        except Exception as e:
            print(e)
            return False
        else:
            sll.add(dvd.name, dvd)
            return True

    def remove(self, dvd):
        sll = self.mux(dvd.name)
        try:
            self.__db.delete(dvd.db_id)
        except Exception as e:
            print(e)
            return False
        else:
            sll.remove(dvd.name)
            return True

    def search(self, name):
        sll = self.mux(name)
        return sll.search(name)

    def update(self, dvd, **kwargs):
        try:
            self.__db.update(dvd.db_id, **kwargs)
        except Exception as e:
            print(e)
            return False
        else:
            for filed, value in kwargs.items():
                setattr(dvd, filed, value)

            return True

    def show_all(self):
        cache = []
        for alpha in self.__mux.alpha_code:
            cache.extend(self.listing(alpha))

        return cache

    def listing(self, prefix):
        cache = []
        for node in self.mux(prefix):
            cache.append(node.value)

        return cache
