from unittest import main, TestCase

from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):

    def setUp(self):
        self.player = TennisPlayer("Rafael Nadal", 34, 10200)

    def test_correct_initialization(self):
        self.assertEqual("Rafael Nadal", self.player.name)
        self.assertEqual(34, self.player.age)
        self.assertEqual(10200, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_setter_with_invalid_value_return_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.player.name = "R1"
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_age_setter_with_invalid_value_return_value_error(self):
        with self.assertRaises(ValueError) as ex:
            self.player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test_age_setter_with_valid_value_return_correct_value(self):
        self.player.age = 18
        self.assertEqual(18, self.player.age)

    def test_add_new_win_with_valid_name_return_message(self):
        self.player.wins.append("Paris")
        self.player.wins.append("Sofia")
        self.player.add_new_win("London")
        result = len(self.player.wins)
        self.assertEqual(3, result)
        self.assertEqual(["Paris", "Sofia", "London"], self.player.wins)

    def test_add_new_win_with_invalid_name_return_message(self):
        self.player.add_new_win("Paris")
        self.assertEqual("Paris has been already added to the list of wins!", self.player.add_new_win("Paris"))
        self.assertEqual(["Paris"], self.player.wins)

    def test_dunder_lt_with_player_with_less_points_return_message(self):
        other_player = TennisPlayer("Grigor Dimitrov", 39, 12000)
        result = self.player < other_player
        self.assertEqual("Grigor Dimitrov is a top seeded player and he/she is better than Rafael Nadal",
                         result)

    def test_dunder_lt_with_player_with_greather_points_return_message(self):
        other_player = TennisPlayer("Grigor Dimitrov", 30, 12000)
        result = self.player > other_player
        self.assertEqual("Grigor Dimitrov is a better player than Rafael Nadal",
                         result)

    def test__str__return_correct_string(self):
        self.player.add_new_win("Paris")
        self.player.add_new_win("Sofia")
        self.assertEqual("Tennis Player: Rafael Nadal\n"
                         "Age: 34\n"
                         "Points: 10200.0\n"
                         "Tournaments won: Paris, Sofia",
                         str(self.player))


if __name__ == '__main__':
    main()
