import unittest
from app import pipeline

class TestSpamClassifier(unittest.TestCase):

    def test_spam_message(self):

        message = ["Congratulations! You won a free iPhone"]

        prediction = pipeline.predict(message)[0]

        self.assertEqual(prediction, 1)


    def test_not_spam_message(self):

        message = ["Hello, how are you doing today?"]

        prediction = pipeline.predict(message)[0]

        self.assertEqual(prediction, 0)


    def test_normal_message(self):

        message = ["Let's meet tomorrow for lunch"]

        prediction = pipeline.predict(message)[0]

        self.assertEqual(prediction, 0)


if __name__ == "__main__":
    unittest.main()