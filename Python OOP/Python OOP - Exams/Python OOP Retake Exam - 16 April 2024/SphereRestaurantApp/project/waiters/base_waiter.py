from abc import ABC, abstractmethod


class BaseWaiter(ABC):
    def __init__(self, name, hours_worked):
        self.name = name
        self.hours_worked = hours_worked

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 3 or len(value) > 50:
            raise ValueError("Waiter name must be between 3 and 50 characters in length!")
        self._name = value

    @property
    def hours_worked(self):
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, value):
        if value < 0:
            raise ValueError("Cannot have negative hours worked!")
        self._hours_worked = value

    @abstractmethod
    def calculate_earnings(self):
        pass

    @abstractmethod
    def report_shift(self):
        pass

    def __str__(self):
        total_earnings = self.calculate_earnings()
        return f"Name: {self.name}, Total earnings: ${total_earnings:.2f}"
    