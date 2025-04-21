from unittest import TestCase

from wordle import confirm_word

class TestConfirmWord(TestCase):
    def test_confirm_word_correct_word(self):
        expected = confirm_word('aaaaa', 'aaaaa')
        actual = (2, 2, 2, 2, 2)
        self.assertEqual(expected, actual)

    def test_confirm_word_correct_letters_wrong_spots(self):
        expected = confirm_word('abcde', 'edbca')
        actual = (1, 1, 1, 1, 1)
        self.assertEqual(expected, actual)

    def test_confirm_word_nothing_correct(self):
        expected = confirm_word('aaaaa', 'bbbbb')
        actual = (0, 0, 0, 0, 0)
        self.assertEqual(expected, actual)

    def test_confirm_word_some_correct_letters_rest_wrong(self):
        expected = confirm_word('aabba', 'ccaac')
        actual = (1, 1, 0, 0, 1)
        self.assertEqual(expected, actual)

    def test_confirm_word_some_correct_letters_rest_right(self):
        expected = confirm_word('abbbc', 'cbbba')
        actual = (1, 2, 2, 2, 1)
        self.assertEqual(expected, actual)

    def test_confirm_word_some_correct_letters_some_right_rest_wrong(self):
        expected = confirm_word('abcde', 'abdcx')
        actual = (2, 2, 1, 1, 0)
        self.assertEqual(expected, actual)

    def test_confirm_word_all_same_letters(self):
        expected = confirm_word('aaaaa', 'aaaaa')
        actual = (2, 2, 2, 2, 2)
        self.assertEqual(expected, actual)

    def test_confirm_word_duplicate_letters(self):
        expected = confirm_word('aabbc', 'aabbb')
        actual = (2, 2, 2, 2, 0)
        self.assertEqual(expected, actual)
