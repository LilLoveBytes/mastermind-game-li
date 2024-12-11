import unittest
from flask import Flask, json
from app.models.gameController import give_feedback
from app import create_app


class GameTestCase(unittest.TestCase):
    def setUp(self):
        testConfig = {
            'TESTING': True,
            'DEBUG': False
        }
        self.app = create_app(testConfig)
        self.client = self.app.test_client()

    def test_give_feedback(self):
        guess = "1351"
        secret_combo = [0, 1, 3, 5]
        guess_array = [1, 3, 5, 1]
        attempts = 1
        feedback = give_feedback(guess, guess_array, secret_combo, attempts)
        expected_feedback = "Your guess [1351] has 3 correct numbers, with 0 in the correct position."
        self.assertEqual(feedback, expected_feedback)

    def test_start_game(self):
        response = self.client.post('/start')
        self.assertEqual(response.status_code, 200)

    def test_submit_guess(self):
        secret_combo = [0, 1, 3, 5]
        game_state = {
            "secret_combo": secret_combo,
            "attempts": 0,
            "guesses": []
        }
        self.client.set_cookie('game_state',
                              json.dumps(game_state))
        response = self.client.post('/guess', json={"guess": "1234"})
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
