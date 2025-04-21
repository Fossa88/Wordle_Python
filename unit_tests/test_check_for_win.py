from unittest import TestCase

from wordle import check_for_win

class TestCheckForWin(TestCase):
    def test_check_for_win_correct_word_first_try(self):
        expected = check_for_win({1: (2, 2, 2, 2, 2)})
        actual = False
        self.assertEqual(expected, actual)

    def test_check_for_win_correct_word_second_try(self):
        expected = check_for_win({1: (0, 1, 1, 2, 1), 2: (2, 2, 2, 2, 2)})
        actual = False
        self.assertEqual(expected, actual)

    def test_check_for_win_correct_word_third_try(self):
        expected = check_for_win({1: (0, 0, 1, 1, 0), 2: (2, 2, 2, 2, 0), 3: (2, 2, 2, 2, 2)})
        actual = False
        self.assertEqual(expected, actual)

    def test_check_for_win_correct_word_fourth_try(self):
        expected = check_for_win({1: (0, 0, 0, 0, 0), 2: (0, 0, 1, 1, 0), 3: (0, 2, 2, 0, 1),
                                  4: (2, 2, 2, 2, 2)})
        actual = False
        self.assertEqual(expected, actual)

    def test_check_for_win_correct_word_fifth_try(self):
        expected = check_for_win({1: (0, 0, 0, 0, 0), 2: (0, 1, 0, 0, 0), 3: (0, 1, 1, 0, 0),
                                  4: (0, 0, 2, 2, 2), 5: (2, 2, 2, 2, 2)})
        actual = False
        self.assertEqual(expected, actual)

    def test_check_for_win_correct_word_sixth_try(self):
        expected = check_for_win({1: (0, 0, 0, 0, 0), 2: (0, 0, 1, 0, 0), 3: (0, 0, 0, 2, 2),
                                  4: (0, 1, 0, 2, 2), 5: (2, 2, 0, 2, 2), 6: (2, 2, 2, 2, 2)})
        actual = False
        self.assertEqual(expected, actual)

    def test_check_for_win_correct_did_not_win(self):
        expected = check_for_win({1: (0, 0, 0, 0, 0), 2: (0, 2, 1, 0, 0), 3: (0, 0, 0, 2, 2),
                                  4: (0, 1, 0, 2, 2), 5: (2, 2, 0, 2, 2), 6: (2, 2, 0, 2, 2)})
        actual = True
        self.assertEqual(expected, actual)

    def test_check_for_win_all_1s(self):
        expected = check_for_win({1: (1, 1, 1, 1, 1)})
        actual = True
        self.assertEqual(expected, actual)

    def test_check_for_win_all_0s(self):
        expected = check_for_win({1: (0, 0, 0, 0, 0)})
        actual = True
        self.assertEqual(expected, actual)

    def test_check_for_win_mixed(self):
        expected = check_for_win({1: (2, 1, 0, 1, 2)})
        actual = True
        self.assertEqual(expected, actual)
