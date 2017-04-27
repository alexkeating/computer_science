from unittest import TestCase
from hypothesis import given
from hypothesis.strategies import lists, integers

from algorithms.merge_sort import merge_sort


class MergeSort(TestCase):

    @given(lists(integers()))
    def test_merge_sort(self, numbers):
        merged_list = merge_sort(numbers)
        sorted_list = sorted(numbers)
        self.assertEqual(merged_list, sorted_list)

