from unittest import TestCase

from wordle import validate_word

class TestValidateWord(TestCase):
    def test_validate_word_is_5_letters_and_in_list_of_words(self):
        expected = validate_word('hello', ['hello', 'pizza', 'bigot'])
        actual = True
        self.assertEqual(expected, actual)

    def test_validate_word_not_5_letters(self):
        expected = validate_word('pair', ['hello', 'pizza', 'bigot'])
        actual = False
        self.assertEqual(expected, actual)

    def test_validate_word_not_in_list_of_words(self):
        expected = validate_word('party', ['hello', 'pizza', 'bigot'])
        actual = False
        self.assertEqual(expected, actual)
