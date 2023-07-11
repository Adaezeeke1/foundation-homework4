import unittest
from assessment2 import is_isogram


class MyTestCase(unittest.TestCase):
    def test_is_isogram(self):
        word = "isogram"
        assert is_isogram(word) == True, f"Test case 1 failed: {word} should be recognized as an isogram."

    def test_mixed_case(self):
        word = "IsOgRaM"
        assert is_isogram(word) == True, f"Test case 2 failed: {word} should be recognized as an isogram."

    def test_repeating_letters(self):
        word = "hello"
        assert is_isogram(word) == False, f"Test case 3 failed: {word} should not be recognized as an isogram."

    def test_repeating_letters_case_insensitive(self):
        word = "HeLLo"
        assert is_isogram(word) == False, f"Test case 4 failed: {word} should not be recognized as an isogram."

    def test_empty_string(self):
        word = ""
        assert is_isogram(word) == True, f"Test case 5 failed: {word} should be recognized as empty."


if __name__ == '__main__':
    unittest.main()

# Explanation for each test case:

# Test 1: This is a basic isogram with all lowercase letters. It tests the function's ability to correctly identify an isogram.

# Test 2: Similar to the first test case, but this time the word has mixed case letters. This test ensures that the function handles case-insensitive comparisons and still identifies the word as an isogram.

# Test 3: This test checks for a non-isogram with repeating letters. It helps verify that the function can correctly detect when a word is not an isogram.

# Test 4: Similar to the previous test case, but with mixed case letters. It confirms that the function correctly handles case-insensitive comparisons even when the word is not an isogram.

# Test 5: This test covers an edge case with an empty string. It ensures that the function can handle empty inputs.