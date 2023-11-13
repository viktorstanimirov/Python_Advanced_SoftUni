from unittest import TestCase, main
from project import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Max", 10)

    def test_correct_initialization(self):
        self.assertEqual("Max", self.driver.name)
        self.assertEqual(10, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_setter_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -10
        self.assertEqual("Max went bankrupt.", str(ve.exception))

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer("Burgas", 2000)

        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()

        self.assertEqual(f"{self.driver.name} went bankrupt.",str(ve.exception))

    def test_earned_money_setter_with_zero_money(self):
        self.assertEqual(0, self.driver.earned_money)
        self.driver.earned_money = 0
        self.assertEqual(0, self.driver.earned_money)

    def test_earned_money_setter(self):
        self.assertEqual(0, self.driver.earned_money)
        self.driver.earned_money = 10
        self.assertEqual(10, self.driver.earned_money)

    def test_add_cargo_offer_raises(self):
        self.assertEqual({}, self.driver.available_cargos)
        self.driver.add_cargo_offer("Sofia", 100)
        self.driver.add_cargo_offer("Plovdiv", 200)
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Sofia", 100)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer(self):
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual("Cargo for 100 to Sofia was added as an offer.", self.driver.add_cargo_offer("Sofia", 100))
        self.assertEqual("Cargo for 200 to Plovdiv was added as an offer.", self.driver.add_cargo_offer("Plovdiv", 200))
        self.assertEqual({"Sofia": 100, "Plovdiv": 200}, self.driver.available_cargos)
        self.assertEqual(2, len(self.driver.available_cargos))

    def test_drive_best_cargo_offer_raises(self):
        self.assertEqual(f"There are no offers available.", self.driver.drive_best_cargo_offer())

    def test_drive_best_cargo_offer(self):
        self.assertEqual("Cargo for 100 to Sofia was added as an offer.", self.driver.add_cargo_offer("Sofia", 100))
        self.assertEqual("Cargo for 200 to Plovdiv was added as an offer.", self.driver.add_cargo_offer("Plovdiv", 200))
        self.assertEqual({"Sofia": 100, "Plovdiv": 200}, self.driver.available_cargos)
        self.assertEqual("Max is driving 200 to Plovdiv.", self.driver.drive_best_cargo_offer())
        self.assertEqual(2_000, self.driver.earned_money)
        self.assertEqual(200, self.driver.miles)

    def test_eat(self):
        self.assertEqual(0, self.driver.earned_money)
        self.driver.earned_money = 2_500
        self.assertEqual(2_500, self.driver.earned_money)
        self.driver.eat(1_250)
        self.assertEqual(2_480, self.driver.earned_money)

    def test_sleep(self):
        self.assertEqual(0, self.driver.earned_money)
        self.driver.earned_money = 2_500
        self.assertEqual(2_500, self.driver.earned_money)
        self.driver.sleep(2_000)
        self.assertEqual(2_455, self.driver.earned_money)

    def test_pump_gas(self):
        self.assertEqual(0, self.driver.earned_money)
        self.driver.earned_money = 2_500
        self.assertEqual(2_500, self.driver.earned_money)
        self.driver.pump_gas(3_000)
        self.assertEqual(2_000, self.driver.earned_money)

    def test_repair_truck(self):
        self.assertEqual(0, self.driver.earned_money)
        self.driver.earned_money = 12_000
        self.assertEqual(12_000, self.driver.earned_money)
        self.driver.repair_truck(20_000)
        self.assertEqual(4_500, self.driver.earned_money)

    def test_activities(self):
        self.assertEqual(0, self.driver.earned_money)
        self.driver.earned_money = 12_000
        TruckDriver.check_for_activities(self.driver, 1000)
        self.assertEqual(11_875, self.driver.earned_money)

    def test_representation(self):
        self.driver.miles = 100
        self.assertEqual(f"Max has 100 miles behind his back.", str(self.driver))

    if __name__ == '__main__':
        main()
