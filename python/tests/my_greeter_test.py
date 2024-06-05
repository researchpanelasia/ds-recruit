import unittest
from src.my_greeter import MyGreeter

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._my_greeter = MyGreeter()

    def test_init(self):
        self.assertIsInstance(self._my_greeter, MyGreeter)

    def test_greeting(self):
        self.assertTrue(len(self._my_greeter.greeting())>0)

if __name__ == '__main__':
    unittest.main()
