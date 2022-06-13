from dataclasses import dataclass


@dataclass
class DVD:
    name: str
    stars: str
    producer: str
    director: str
    production_company: str
    copies: int
    total_quantity: int
    db_id: int = 0

    def __str__(self):
        return (
            f'name: {self.name} | is_available: {self.isavailable}'
        )

    @property
    def isavailable(self):
        return self.copies > 0

    def rented(self) -> bool:
        if self.isavailable:
            self.copies -= 1
            return True
        else:
            return False

    def checked_out(self) -> bool:
        if self.copies == self.total_quantity:
            return False
        else:
            self.copies += 1
            return True
