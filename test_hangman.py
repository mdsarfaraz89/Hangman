import unittest
from hangman import mask_word, validate_guess, has_won, choose_word, WORDS


class TestHangman(unittest.TestCase):
    def test_mask_word(self):
        self.assertEqual(mask_word("cat", {"c", "t"}), "c _ t")

    def test_mask_word_nothing_guessed(self):
        self.assertEqual(mask_word("ab", set()), "_ _")

    def test_validate_guess(self):
        self.assertFalse(validate_guess("", set())[0])
        self.assertFalse(validate_guess("ab", set())[0])
        self.assertFalse(validate_guess("1", set())[0])
        self.assertFalse(validate_guess("a", {"a"})[0])
        self.assertTrue(validate_guess("a", set())[0])

    def test_has_won(self):
        self.assertTrue(has_won("hi", {"h", "i"}))
        self.assertFalse(has_won("hi", {"h"}))

    def test_choose_word(self):
        self.assertIn(choose_word(), WORDS)


if __name__ == "__main__":
    unittest.main()
