import copy
from typing import List

from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: List = []
        self.vehicles: List = []
        self.routes: List = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str) -> str:
        for user in self.users:
            if user.driving_license_number == driving_license_number:
                return f"{driving_license_number} has already been registered to our platform."

        create_user = User(first_name, last_name, driving_license_number)
        self.users.append(create_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str) -> str:
        if vehicle_type not in ["PassengerCar", "CargoVan"]:
            return f"Vehicle type {vehicle_type} is inaccessible."

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                return f"{license_plate_number} belongs to another vehicle."

        car_types = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}
        create_vehicle = car_types[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(create_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float) -> str:
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point:
                if route.length == length:
                    return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                elif route.length < length:
                    return f"{start_point}/{end_point} shorter route had already been added to our platform."
                elif route.length > length:
                    route.is_locked = True

        curr_route = Route(start_point, end_point, length, len(self.routes) + 1)
        self.routes.append(curr_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        current_user, current_vehicle, current_route = None, None, None

        for user in self.users:
            if user.driving_license_number == driving_license_number:
                if user.is_blocked:
                    return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
                current_user = user

        for vehicle in self.vehicles:
            if vehicle.license_plate_number == license_plate_number:
                if vehicle.is_damaged:
                    return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
                current_vehicle = vehicle

        for route in self.routes:
            if route.route_id == route_id:
                if route.is_locked:
                    return f"Route {route_id} is locked! This trip is not allowed."
                current_route = route

        current_vehicle.drive(current_route.length)

        if is_accident_happened:
            current_vehicle.is_damaged = True
            current_user.decrease_rating()

        else:
            current_user.increase_rating()

        if current_vehicle.is_damaged:
            damage_status = "Damaged"
        else:
            damage_status = "OK"
        return f"{current_vehicle.brand} {current_vehicle.model} License plate: {license_plate_number} " \
               f"Battery: {current_vehicle.battery_level}% Status: {damage_status}"

    def repair_vehicles(self, count: int):
        damaged_vehicles = sorted([car for car in self.vehicles if car.is_damaged], key=lambda x: (x.brand, x.model))
        damage_cars_count = damaged_vehicles[:count]

        for car in damage_cars_count:
            car.is_damaged = False
            car.battery_level = 100

        return f"{len(damage_cars_count)} vehicles were successfully repaired!"

    def users_report(self):
        report_users = copy.copy(self.users)
        report_users = sorted(report_users, key=lambda k: -k.rating)
        print_result = '\n'.join([str(x) for x in report_users])

        return f"*** E-Drive-Rent ***\n{print_result}"
