import math
import unittest

def calcCircumfrence(r):
    return r*2*math.pi

print(calcCircumfrence(5))

# unit testing class
class TestMyClass(unittest.TestCase):
    # Need to define funcction name with test_name_of_function
    
    # first test case 
    def test_circumferenceOne(self):
        self.assertEqual(calcCircumfrence(5),31.41592653589793)

    # second test case 
    def test_circumferenceTwo(self):
        self.assertEqual(calcCircumfrence(0),0)

if __name__ == '__main__':
    unittest.main()
