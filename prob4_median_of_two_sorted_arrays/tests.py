import unittest
from solution import Solution

class TestMedianOfTwoSortedArrays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.findMedianSortedArrays([1, 3], [2]), 2.0)

    def test_example_2(self):
        self.assertEqual(self.solution.findMedianSortedArrays([1, 2], [3, 4]), 2.5)

    def test_empty_first_array(self):
        self.assertEqual(self.solution.findMedianSortedArrays([], [1]), 1.0)

    def test_empty_second_array(self):
        self.assertEqual(self.solution.findMedianSortedArrays([2], []), 2.0)

    def test_both_empty_arrays(self):
        with self.assertRaises(ValueError):
            self.solution.findMedianSortedArrays([], [])

    def test_large_input(self):
        nums1 = list(range(1000))
        nums2 = list(range(1000, 2000))
        self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), 999.5)

if __name__ == "__main__":
    unittest.main()
