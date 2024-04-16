from abc import ABC, abstractmethod


class BaseClient(ABC):
    ALLOWED_MEMBERSHIP_TYPES = [
        "Regular", "VIP"
    ]

    def __init__(self, name, membership_type, points=0):
        self.name = name
        self.membership_type = membership_type
        self.points = points

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Client name should be determined!")

        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in BaseClient.ALLOWED_MEMBERSHIP_TYPES:
            raise ValueError("Invalid membership type. Allowed types: Regular, VIP.")
        self._membership_type = value

    @abstractmethod
    def earning_points(self, order_amount):
        pass

    def apply_discount(self):
        if self.points >= 100:
            discount_percentage = 10
            used_points = 100
        elif self.points >= 50:
            discount_percentage = 5
            used_points = 50
        else:
            discount_percentage = 0
            used_points = 0

        self.points -= used_points
        return (discount_percentage, self.points)
