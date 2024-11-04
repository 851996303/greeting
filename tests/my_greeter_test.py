import unittest
from datetime import datetime
from unittest.mock import patch

from src.my_greeter import MyGreeter

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._my_greeter = MyGreeter()

    def test_init(self):
        self.assertIsInstance(self._my_greeter, MyGreeter)

    @patch('src.my_greeter.datetime')
    def test_greeting_morning(self, test_datetime):
        test_datetime.now.return_value = datetime(2024, 11, 4, 10)
        self.assertEqual(self._my_greeter.greeting(), 'Good morning')

    @patch('src.my_greeter.datetime')
    def test_greeting_afternoon(self, test_datetime):
        test_datetime.now.return_value = datetime(2024, 11, 4, 14)
        self.assertEqual(self._my_greeter.greeting(), 'Good afternoon')

    @patch('src.my_greeter.datetime')
    def test_greeting_evening(self, test_datetime):
        test_datetime.now.return_value = datetime(2024, 11, 4, 20)
        self.assertEqual(self._my_greeter.greeting(), 'Good evening')

if __name__ == '__main__':
    unittest.main()