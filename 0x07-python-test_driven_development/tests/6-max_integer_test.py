#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from your_module_name import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test case 1: Check if the function returns the correct maximum value
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test case 2: Check if the function handles a reversed list correctly
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

        # Test case 3: Check if the function handles a list with negative numbers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test case 4: Check if the function handles a list with duplicates
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

        # Test case 5: Check if the function handles an empty list (should return None)
        self.assertIsNone(max_integer([]))

if __name__ == "__main__":
    unittest.main()
#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from your_module_name import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test case 1: Check if the function returns the correct maximum value
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test case 2: Check if the function handles a reversed list correctly
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

        # Test case 3: Check if the function handles a list with negative numbers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test case 4: Check if the function handles a list with duplicates
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

        # Test case 5: Check if the function handles an empty list (should return None)
        self.assertIsNone(max_integer([]))

if __name__ == "__main__":
    unittest.main()

