from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    def __init__(self, name):
        super().__init__(name, "Regular")

    def earning_points(self, order_amount):
        earned_points = int(order_amount // 10)
        self.points += earned_points
        return earned_points

    def display_info(self):
        print(f"Client Name: {self.name}")
        print(f"Membership Type: {self.membership_type}")
        print(f"Total Points: {self.points}")
