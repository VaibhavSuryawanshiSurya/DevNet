import unittest
from prime_number import is_prime_number


# unit testing class
class TestPrimeNumber(unittest.TestCase):
    # Need to define funcction name with test_name_of_function

    def test_is_prime_number_one(self):
        self.assertEqual(is_prime_number(5), True)

    def test_is_prime_number_two(self):
        self.assertEqual(is_prime_number(4),False)

if __name__ == '__main__':
    unittest.main()