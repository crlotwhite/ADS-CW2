from common.ads.bst import BinarySearchTree
from common.mux import AlphaMux
from common.metaclass.singleton import SingletonMetaclass
from customer.db import CustomerController


class CustomerBTreeType(metaclass=SingletonMetaclass):
    def __init__(self):
        self.__mux = AlphaMux(BinarySearchTree)
        self.__db = CustomerController()

        print('loading customer data from db...')
        for customer in self.__db.fetch_all():
            bst = self.mux(customer.name)
            bst.add(customer.name, customer)
        else:
            print('loaded customer data successfully!')

    def mux(self, name):
        return self.__mux.mux(name)

    def add(self, customer):
        bst = self.mux(customer.name)
        try:
            customer.db_id = self.__db.add(customer.name)
        except Exception as e:
            print(e)
            return False
        else:
            bst.add(customer.name, customer)
            return True

    def remove(self, name):
        bst = self.mux(name)
        try:
            result = self.search(name)
            self.__db.delete(result.db_id)
        except Exception as e:
            print(e)
            return False
        else:
            bst.remove(name)
            return True

    def search(self, name):
        bst = self.mux(name)
        return bst.value_of(name)

    def update(self, customer, **kwargs):
        try:
            self.__db.update(customer.db_id, **kwargs)
        except Exception as e:
            print(e)
            return False
        else:
            for filed, value in kwargs.items():
                setattr(customer, filed, value)

            return True
