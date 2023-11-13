from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = {
        "MainService": MainService,
        "SecondaryService": SecondaryService
    }

    VALID_ROBOT_TYPES = {
        "MaleRobot": MaleRobot,
        "FemaleRobot": FemaleRobot
    }

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str) -> str:
        if service_type not in RobotsManagingApp.VALID_SERVICE_TYPES.keys():
            raise Exception("Invalid service type!")

        service = RobotsManagingApp.VALID_SERVICE_TYPES[service_type](name)
        self.services.append(service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float) -> str:
        if robot_type not in RobotsManagingApp.VALID_ROBOT_TYPES.keys():
            raise Exception("Invalid robot type!")

        robot = RobotsManagingApp.VALID_ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str) -> str:
        robot = self.find_robot(robot_name)
        service = self.find_service(service_name)

        if ((robot.__class__.__name__ == "FemaleRobot" and service.__class__.__name__ == "MainService") or
                (robot.__class__.__name__ == "MaleRobot" and service.__class__.__name__ == "SecondaryService")):
            return f"Unsuitable service."

        if len(service.robots) == service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str) -> str:
        service = self.find_service(service_name)
        robot = [r for r in service.robots if r.name == robot_name]

        if not robot:
            raise Exception("No such robot in this service!")
        current_robot = robot[0]

        service.robots.remove(current_robot)
        self.robots.append(current_robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str) -> str:
        service = self.find_service(service_name)
        number_of_robots_fed = 0
        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str) -> str:
        total_service_price = sum([r.price for r in self.find_service(service_name).robots])

        return f"The value of service {service_name} is {total_service_price:.2f}."

    def __str__(self):
        return "\n".join([s.details() for s in self.services])

    def find_robot(self, robot_name: str):
        robot = [r for r in self.robots if r.name == robot_name][0]
        return robot

    def find_service(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        return service
