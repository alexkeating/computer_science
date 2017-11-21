import unittest

from questions.arrays.questions import (check_permutations,
                                        string_is_unique,
                                        urlify)


class ArrayQuestionsTest(unittest.TestCase):

    def test_string_is_unique_blank(self):
        string = ''
        is_unique = string_is_unique(string)
        self.assertEqual(True, is_unique)

    def test_string_is_not_unique(self):
        string = 'alabama'
        is_unique = string_is_unique(string)
        self.assertEqual(False, is_unique)

    def test_string_is_unique(self):
        string = 'abcdefghijklmnopqrstuvwxyz'
        is_unique = string_is_unique(string)
        self.assertEqual(True, is_unique)

    def test_check_permutations_blanks(self):
        string_one = ''
        string_two = ''
        is_permutation = check_permutations(string_one, string_two)
        self.assertEqual(True, is_permutation)

    def test_check_permutations_not_permutaion(self):
        string_one = 'alex'
        string_two = 'alax'
        is_permutation = check_permutations(string_one, string_two)
        self.assertEqual(False, is_permutation)

    def test_check_permutations_different_length(self):
        string_one = 'pete'
        string_two = 'pet'
        is_permutation = check_permutations(string_one, string_two)
        is_permutation_reverse = check_permutations(string_two, string_one)
        self.assertEqual(False, is_permutation)
        self.assertEqual(False, is_permutation_reverse)

    def test_check_permutations_permutation(self):
        string_one = 'tab'
        string_two = 'bat'
        is_permutation = check_permutations(string_one, string_two)
        self.assertEqual(True, is_permutation)

    def test_urlify_none(self):
        string = None
        new_string = urlify(string, 0)
        self.assertEqual(None, new_string)

    def test_urlify_no_spaces(self):
        string = 'albert'
        new_string = urlify(string, 6)
        self.assertEqual(string, new_string)

    def test_urlify_with_spaces(self):
        string = 'He was a great  man! '
        new_string = urlify(string, 20)
        self.assertEqual(new_string, 'He%20was%20a%20great%20man!%20')
