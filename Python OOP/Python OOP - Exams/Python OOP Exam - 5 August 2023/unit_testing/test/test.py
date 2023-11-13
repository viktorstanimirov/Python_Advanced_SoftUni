from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar("BMW", "X5", 12000, 30000)

    def test_correct_initialization(self):
        self.assertEqual("BMW", self.car.model)
        self.assertEqual("X5", self.car.car_type)
        self.assertEqual(12000, self.car.mileage)
        self.assertEqual(30000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setrer_with_negative_value_raise(self):
        with self.assertRaises(ValueError) as va:
            self.car.price = -1
        self.assertEqual("Price should be greater than 1.0!", str(va.exception))

    def test_price_with_correct_value(self):
        self.car.price = 2000
        self.assertEqual(2000, self.car.price)

    def test_mileage_setter_with_negative_value_raise(self):
        with self.assertRaises(ValueError) as va:
            self.car.mileage = 100
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(va.exception))

    def test_mileage_with_correct_value(self):
        self.car.mileage = 200
        self.assertEqual(200, self.car.mileage)

    def test_set_promotional_price_with_correct_value(self):
        result = self.car.set_promotional_price(10000)
        self.assertEqual("The promotional price has been successfully set.", result)
        self.assertEqual(10000, self.car.price)

    def test_set_promotional_price_with_incorrect_value(self):
        with self.assertRaises(ValueError) as va:
            self.car.set_promotional_price(40000)
        self.assertEqual("You are supposed to decrease the price!", str(va.exception))

    def test_need_repair_not_done_message(self):
        self.car.price = 15000
        result = self.car.need_repair(10000, "tyres")
        self.assertEqual("Repair is impossible!", result)

    def test_need_repair_done_message(self):
        self.car.price = 15000
        result = self.car.need_repair(1000, "tyres")
        self.assertEqual("Price has been increased due to repair charges.", result)
        self.assertEqual(16000, self.car.price)
        self.assertEqual(["tyres"], self.car.repairs)

    def test_gt_with_different_car_type(self):
        other = SecondHandCar("Audi", "A3", 12000, 30000)
        result = self.car > other
        self.assertEqual("Cars cannot be compared. Type mismatch!", result)

    def test_gt_with_correct_value(self):
        other = SecondHandCar("BMW", "X5", 12000, 20000)
        result = self.car > other
        self.assertEqual(True, result)

    def test_str_method(self):
        result = str(self.car)
        self.assertEqual("""Model BMW | Type X5 | Milage 12000km
Current price: 30000.00 | Number of Repairs: 0""", result)


if __name__ == '__main__':
    main()
