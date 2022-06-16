from dataclasses import (
    dataclass,
    field
)
from typing import List


@dataclass
class Customer:
    name: str
    rented_dvd: List[str]
    db_id: int = 0

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return (
            f'id: {self.db_id} | name: {self.name} | rented_dvd: {self.rented_dvd_str}'
        )

    @property
    def account_id(self):
        return hash(self.name)

    @property
    def rented_dvd_str(self):
        return ','.join(self.rented_dvd)

    def rent(self, dvd):
        if dvd.rented():
            self.rented_dvd.append(dvd.name)
            return True
        else:
            return False

    def check_out(self, dvd):
        if dvd.checked_out():
            self.rented_dvd.remove(dvd.name)
            return True
        else:
            return False

