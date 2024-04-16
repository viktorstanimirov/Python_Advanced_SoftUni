from project.waiters.base_waiter import BaseWaiter


class FullTimeWaiter(BaseWaiter):
    FULL_TIME_HOURLY_WAGE = 15.0

    def __init__(self, name, hours_worked):
        super().__init__(name, hours_worked)

    def calculate_earnings(self):
        return self.hours_worked * FullTimeWaiter.FULL_TIME_HOURLY_WAGE

    def report_shift(self):
        return f"{self.name} worked a full-time shift of {self.hours_worked} hours."
