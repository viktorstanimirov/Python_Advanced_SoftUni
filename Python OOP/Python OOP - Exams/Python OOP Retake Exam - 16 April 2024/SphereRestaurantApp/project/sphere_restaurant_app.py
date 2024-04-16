from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    VALID_WAITHER_TYPES = {
        "FullTimeWaiter": FullTimeWaiter,
        "HalfTimeWaiter": HalfTimeWaiter,
    }

    VALID_CLIENT_TYPES = {
        "RegularClient": RegularClient,
        "VIPClient": VIPClient,
    }

    def __init__(self):
        self.waiters = []
        self.clients = []

    def hire_waiter(self, waiter_type, waiter_name, hours_worked):
        if waiter_type not in SphereRestaurantApp.VALID_WAITHER_TYPES:
            return f"{waiter_type} is not a recognized waiter type."

        if waiter_name in [w.name for w in self.waiters]:
            return f"{waiter_name} is already on the staff."

        curr_waiter = self.VALID_WAITHER_TYPES[waiter_type](waiter_name, hours_worked)
        self.waiters.append(curr_waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type, client_name):
        if client_type not in SphereRestaurantApp.VALID_CLIENT_TYPES:
            return f"{client_type} is not a recognized client type."

        if client_name in [c.name for c in self.clients]:
            return f"{client_name} is already a client."

        curr_client = self.VALID_CLIENT_TYPES[client_type](client_name)
        self.clients.append(curr_client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        for waiter in self.waiters:
            if waiter.name == waiter_name:
                return waiter.report_shift()
        return f"No waiter found with the name {waiter_name}."

    def process_client_order(self, client_name: str, order_amount: float):
        for client in self.clients:
            if client.name == client_name:
                points_earned = client.earning_points(order_amount)
                return f"{client_name} earned {points_earned} points from the order."
        return f"{client_name} is not a registered client."

    def apply_discount_to_client(self, client_name: str):
        for client in self.clients:
            if client.name == client_name:
                discount_percentage, remaining_points = client.apply_discount()
                return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"
        return f"{client_name} cannot get a discount because this client is not admitted!"

    def generate_report(self):
        total_earnings = sum(waiter.calculate_earnings() for waiter in self.waiters)
        total_client_points = sum(client.points for client in self.clients)
        clients_count = len(self.clients)

        waiters_details = "\n".join(
            f"Name: {waiter.name}, Total earnings: ${waiter.calculate_earnings():.2f}" for waiter in
            sorted(self.waiters, key=lambda w: w.calculate_earnings(), reverse=True))

        report = (f"$$ Monthly Report $$\n"
                  f"Total Earnings: ${total_earnings:.2f}\n"
                  f"Total Clients Unused Points: {total_client_points}\n"
                  f"Total Clients Count: {clients_count}\n"
                  f"** Waiter Details **\n"
                  f"{waiters_details}")
        return report








# sphere_restaurant_app = SphereRestaurantApp()
#
# # Hire some waiters
# print(sphere_restaurant_app.hire_waiter("FullTimeWaiter", "John", 40))
# print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Alice", 20))
# print(sphere_restaurant_app.hire_waiter("InvalidWaiter", "JohnDoe", 10))
# print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Charlie", 30))
# print(sphere_restaurant_app.hire_waiter("FullTimeWaiter", "Frank", 50))
# print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Alice", 60))
#
# # Admit some clients
# print(sphere_restaurant_app.admit_client("InvalidClient", "JohnDoe"))
# print(sphere_restaurant_app.admit_client("VIPClient", "Eve"))
# print(sphere_restaurant_app.admit_client("VIPClient", "Lila"))
# print(sphere_restaurant_app.admit_client("RegularClient", "Bob"))
# print(sphere_restaurant_app.admit_client("VIPClient", "Eve"))
# print(sphere_restaurant_app.admit_client("RegularClient", "Oscar"))
#
# # Process shifts
# print(sphere_restaurant_app.process_shifts("John"))
# print(sphere_restaurant_app.process_shifts("Alice"))
# print(sphere_restaurant_app.process_shifts("Emily"))
# print(sphere_restaurant_app.process_shifts("Frank"))
#
# # Process client orders
# print(sphere_restaurant_app.process_client_order("Bob", 100.0))
# print(sphere_restaurant_app.process_client_order("Eve", 500.0))
# print(sphere_restaurant_app.process_client_order("JohnDoe", 250.0))
# print(sphere_restaurant_app.process_client_order("Bob", 750.0))
# print(sphere_restaurant_app.process_client_order("Lila", 550.0))
# print(sphere_restaurant_app.process_client_order("Oscar", 84.0))
#
# # Apply discounts to clients
# print(sphere_restaurant_app.apply_discount_to_client("Lila"))
# print(sphere_restaurant_app.apply_discount_to_client("Eve"))
# print(sphere_restaurant_app.apply_discount_to_client("JohnDoe"))
# print(sphere_restaurant_app.apply_discount_to_client("Oscar"))
# print(sphere_restaurant_app.apply_discount_to_client("Bob"))
#
# # Generate report
# print(sphere_restaurant_app.generate_report())
