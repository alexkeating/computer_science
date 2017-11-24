import unittest

from data_structures.linked_list import LinkedList
from questions.linked_list.questions import remove_dups


def insert_values(linked_list, values_list):

    for value in values_list:
        linked_list.insert(value)
        new_linked_list = remove_dups(linked_list)
    return new_linked_list


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
