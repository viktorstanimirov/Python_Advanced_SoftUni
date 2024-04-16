from unittest import TestCase, main

from project.restaurant import Restaurant


class TestRestaurant(TestCase):

    def setUp(self):
        self.restaurant = Restaurant("Test", 20)

    def test_correct_initialization(self):
        self.assertEqual("Test", self.restaurant.name)
        self.assertEqual(20, self.restaurant.capacity)
        self.assertEqual([], self.restaurant.waiters)

    def test_name_setter_with_invalid_value_return_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.restaurant.name = ""
        self.assertEqual("Invalid name!", str(ex.exception))

    def test_capacity_setter_with_invalid_value_return_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.restaurant.capacity = -1
        self.assertEqual("Invalid capacity!", str(ex.exception))

    def test_get_waiters_with_no_limits_of_money_earning(self):
        self.restaurant.add_waiter("John")
        self.restaurant.add_waiter("Jane")
        self.restaurant.waiters[0]['total_earnings'] = 150
        self.restaurant.waiters[1]['total_earnings'] = 250

        result = self.restaurant.get_waiters()
        self.assertEqual(2, len(result))
        self.assertEqual([{'name': 'John', 'total_earnings': 150}, {'name': 'Jane', 'total_earnings': 250}], result)

    def test_get_waiters_with_min_money_earning(self):
        self.restaurant.add_waiter("John")
        self.restaurant.add_waiter("Jane")
        self.restaurant.waiters[0]['total_earnings'] = 150
        self.restaurant.waiters[1]['total_earnings'] = 250

        result = self.restaurant.get_waiters(min_earnings=200)
        self.assertEqual(1, len(result))
        self.assertEqual([{'name': 'Jane', 'total_earnings': 250}], result)

    def test_get_waiters_with_max_money_earning(self):
        self.restaurant.add_waiter("John")
        self.restaurant.add_waiter("Jane")
        self.restaurant.waiters[0]['total_earnings'] = 150
        self.restaurant.waiters[1]['total_earnings'] = 250

        result = self.restaurant.get_waiters(max_earnings=200)
        self.assertEqual(1, len(result))
        self.assertEqual([{'name': 'John', 'total_earnings': 150}], result)

    def test_add_waiter_with_full_capacity_return_value_error(self):
            self.restaurant.capacity = 1
            self.restaurant.add_waiter("John")
            result = self.restaurant.add_waiter("Alice")
            self.assertEqual("No more places!", result)

    def test_add_waiter_with_existing_waiter_return_value_error(self):
        self.restaurant.add_waiter("John")
        result = self.restaurant.add_waiter("John")
        self.assertEqual("The waiter John already exists!", result)

    def test_add_waiter_with_valid_data(self):
        result = self.restaurant.add_waiter("John")
        self.assertEqual("The waiter John has been added.", result)
        self.assertEqual([{'name': 'John'}], self.restaurant.waiters)

    def test_remove_waiter_with_existing_waiter(self):
        self.restaurant.add_waiter("John")
        result = self.restaurant.remove_waiter("John")
        self.assertEqual("The waiter John has been removed.", result)
        self.assertEqual([], self.restaurant.waiters)

    def test_remove_waiter_with_non_existing_waiter(self):
        result = self.restaurant.remove_waiter("John")
        self.assertEqual("No waiter found with the name John.", result)

    def test_get_total_earnings(self):
        self.restaurant.add_waiter("John")
        self.restaurant.add_waiter("Jane")
        self.restaurant.waiters[0]['total_earnings'] = 150
        self.restaurant.waiters[1]['total_earnings'] = 250

        result = self.restaurant.get_total_earnings()
        self.assertEqual(400, result)


if __name__ == '__main__':
    main()
