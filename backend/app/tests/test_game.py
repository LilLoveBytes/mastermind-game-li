import unittest
from flask import Flask
from app.models.gameController import give_feedback

class GameTestCase(unittest.TestCase):
  def setUp(self):
    self.app = Flask(__name__)
    self.client = self.app.test_client()
    self.app.config['TESTING'] = True
  
  def test_submit_guess(self):
    guess = "1351"
    secret_combo = [0,1,3,5]
    guess_array = [1,3,5,1]
    attempts = 1
    feedback = give_feedback(guess, guess_array, secret_combo, attempts)
    expected_feedback = "Your guess [1351] has 3 correct numbers, with 0 in the correct position."
    self.assertEqual(feedback, expected_feedback)
  
if __name__ == '__main__':
  unittest.main()