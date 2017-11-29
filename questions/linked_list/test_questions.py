import unittest

from data_structures.linked_list import LinkedList
from questions.linked_list.questions import (delete_middle_node,
                                             remove_dups,
                                             return_kth_to_last,
                                             sum_lists)


def insert_values(linked_list, values_list):

    for value in values_list:
        linked_list.insert(value)
        new_linked_list = remove_dups(linked_list)
    return new_linked_list


def insert_values_dups(linked_list, values_list):

    for value in values_list:
        linked_list.insert(value)
    return linked_list


def get_linked_list_values(linked_list):
    values = []
    node = linked_list.head
    for _ in range(0, linked_list.size()):
        if node:
            values.append(node.data)
            node = node.get_next_node()
    return values


class LinkedListQuestionsTest(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_no_dups(self):
        data_values = ['a', 'b', 'c', 'd', 'e']
        new_linked_list = insert_values(self.linked_list, data_values)
        values = get_linked_list_values(new_linked_list)
        self.assertEqual(sorted(values), sorted(data_values))

    def test_duplicates(self):
        data_values = ['a', 'b', 'b', 'c', 'd', 'e']
        new_linked_list = insert_values(self.linked_list, data_values)
        values = get_linked_list_values(new_linked_list)
        self.assertEqual(sorted(values), ['a', 'b', 'c', 'd', 'e'])

    def test_three_of_the_same(self):
        data_values = ['a', 'b', 'b', 'c', 'd', 'e', 'b']
        new_linked_list = insert_values(self.linked_list, data_values)
        values = get_linked_list_values(new_linked_list)
        self.assertEqual(sorted(values), ['a', 'b', 'c', 'd', 'e'])

    def test_two_duplicates(self):
        data_values = ['a', 'b', 'b', 'c', 'd', 'e', 'b', 'a']
        new_linked_list = insert_values(self.linked_list, data_values)
        values = get_linked_list_values(new_linked_list)
        self.assertEqual(sorted(values), ['a', 'b', 'c', 'd', 'e'])

    def test_return_kth(self):
        data_values = ['a', 'b', 'c', 'e']
        new_linked_list = insert_values(self.linked_list, data_values)
        kth = return_kth_to_last(new_linked_list)
        self.assertEqual(kth.data, 'b')

    def test_return_kth_single_node(self):
        data_values = ['b']
        new_linked_list = insert_values(self.linked_list, data_values)
        kth = return_kth_to_last(new_linked_list)
        self.assertEqual(kth.data, 'b')

    def test_return_kth_none(self):
        kth = return_kth_to_last(None)
        self.assertEqual(kth, None)

    def test_delete_middle_node(self):
        data_values = ['a', 'b', 'c', 'e']
        new_linked_list = insert_values(self.linked_list, data_values)
        node = new_linked_list.search('c')
        delete_middle_node(node)
        values = get_linked_list_values(new_linked_list)
        self.assertEqual(['e', 'b', 'a'], values)

    def test_delete_middle_node_empty(self):
        data_values = ['a', 'b', 'c', 'e']
        new_linked_list = insert_values(self.linked_list, data_values)
        node = None
        delete_middle_node(node)
        values = get_linked_list_values(new_linked_list)
        self.assertEqual(['e', 'c', 'b', 'a'], values)

    def test_sum_lists(self):
        data_values1 = [7, 0, 0]
        data_values2 = [3, 0, 0]

        new_linked_list1 = insert_values_dups(self.linked_list, data_values1)
        new_linked_list2 = insert_values_dups(LinkedList(), data_values2)

        summation = sum_lists(new_linked_list1, new_linked_list2)
        self.assertEqual(1000, summation)

    def test_sum_lists_all_non_zero(self):
        data_values1 = [7, 2, 1]
        data_values2 = [3, 3, 3]

        new_linked_list1 = insert_values_dups(self.linked_list, data_values1)
        new_linked_list2 = insert_values_dups(LinkedList(), data_values2)

        summation = sum_lists(new_linked_list1, new_linked_list2)
        self.assertEqual(1054, summation)

    def test_sum_lists_all_zero(self):
        data_values1 = [0, 0, 0]
        data_values2 = [0, 0, 0]

        new_linked_list1 = insert_values_dups(self.linked_list, data_values1)
        new_linked_list2 = insert_values_dups(LinkedList(), data_values2)

        summation = sum_lists(new_linked_list1, new_linked_list2)
        self.assertEqual(0, summation)
