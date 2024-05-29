import unittest
from solution import Solution

class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)

    def test_empty_string(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

    def test_single_character(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("a"), 1)

    def test_mixed_characters(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("a1b2c3d4e5"), 10)

if __name__ == "__main__":
    unittest.main()
