from project.waiters.base_waiter import BaseWaiter


class HalfTimeWaiter(BaseWaiter):
    HALF_TIME_HOURLY_WAGE = 12.0

    def __init__(self, name: str, hours_worked: int):
        super().__init__(name, hours_worked)

    def calculate_earnings(self):
        return self.hours_worked * HalfTimeWaiter.HALF_TIME_HOURLY_WAGE

    def report_shift(self):
        return f"{self.name} worked a half-time shift of {self.hours_worked} hours."
