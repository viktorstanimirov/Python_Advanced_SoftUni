from unittest import TestCase, main

from project.robot import Robot


class TestRobot(TestCase):
    def setUp(self):
        self.robot = Robot("war", "Military", 10, 10.50)

    def test_constant_atributes_ALLOWED_CATEGORIES(self):
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], Robot.ALLOWED_CATEGORIES)

    def test_constant_atributes_PRICE_INCREMENT(self):
        self.assertEqual(1.5, Robot.PRICE_INCREMENT)

    def test_correct_initialization(self):
        self.assertEqual("war", self.robot.robot_id)
        self.assertEqual("Military", self.robot.category)
        self.assertEqual(10, self.robot.available_capacity)
        self.assertEqual(10.50, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_robot_not_allowed_category(self):
        with self.assertRaises(ValueError) as ve:
            self.robot = Robot("war", "War", 10, 10.50)
        self.assertEqual(f"Category should be one "
                         f"of '{Robot.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_deffaut_price_increment_class_attribute_is_correct(self):
        with self.assertRaises(ValueError) as ve:
            self.robot = Robot("war", "Military", 10, -1)
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_update_hardware_not_in_hardware_updates_not_updated(self):
        self.robot.hardware_upgrades.append("Gun")

        result = self.robot.upgrade("Gun", 10)
        self.assertEqual(f"Robot {self.robot.robot_id} "
                         f"was not upgraded.", result)

    def test_update_hardware_add_hardware_component_and_update_price(self):
        self.robot.hardware_upgrades.append("Gun")
        hardware = "Shootgun"
        result = self.robot.upgrade("Shootgun", 10)
        self.assertEqual(f'Robot {self.robot.robot_id} was upgraded with {hardware}.', result)

    def test_software_not_update(self):
        result = self.robot.update(1.0, 15)
        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", result)

    def test_update_lower_version_and_enough_capacity_software_not_update(self):
        self.robot = Robot('war', 'Education', 200, 100)
        self.robot.update(2.0, 50)
        self.assertEqual(self.robot.software_updates, [2.0])
        result = self.robot.update(1.9, 50)
        self.assertEqual('Robot war was not updated.',result)
        self.assertEqual(self.robot.software_updates, [2.0])
        self.assertEqual(self.robot.available_capacity, 150)

    def test_software_success_update(self):
        result = self.robot.update(1.0, 10)
        self.assertEqual(f"Robot {self.robot.robot_id} was updated to version 1.0.", result)
        self.assertEqual([1.0], self.robot.software_updates)

    def test_dunder_method_gt_self_price_greater_then_other_price(self):
        self.robot2 = Robot("theacer", "Education", 10, 9.5)
        result = self.robot.__gt__(self.robot2)
        self.assertEqual(f'Robot with ID {self.robot.robot_id} is more '
                         f'expensive than Robot with ID {self.robot2.robot_id}.', result)

    def test_dunder_method_gt_self_price_equal_then_other_price(self):
        self.robot2 = Robot("theacer", "Education", 10, 10.50)
        result = self.robot.__gt__(self.robot2)
        self.assertEqual(f'Robot with ID {self.robot.robot_id} '
                         f'costs equal to Robot with ID {self.robot2.robot_id}.', result)

    def test_dunder_method_gt_self_price_is_smaller_then_other_robot_price(self):
        self.robot2 = Robot("theacer", "Education", 10, 11.00)
        result = self.robot.__gt__(self.robot2)
        self.assertEqual(f'Robot with ID {self.robot.robot_id} '
                         f'is cheaper than Robot with ID {self.robot2.robot_id}.', result)


if __name__ == '__main__':
    main()
