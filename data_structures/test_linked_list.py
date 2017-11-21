import unittest

from data_structures.linked_list import (LinkedList,
                                         Node)


class NodeTest(unittest.TestCase):

    def setUp(self):
        self.node = Node('test')

    def test_get_data(self):
        self.assertEquals('test', self.node.get_data())

    def test_get_next_node_none(self):
        self.assertEquals(None, self.node.get_next_node())

    def test_get_next_node_value(self):
        new_node = Node('test2')
        self.node.set_next_node(new_node)
        self.assertEquals('test2', self.node.get_next_node().get_data())


class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_insert(self):
        self.linked_list.insert('test')
        self.assertEquals(self.linked_list.head.get_data(), 'test')

    def test_size(self):
        self.linked_list.insert('test')
        self.assertEquals(self.linked_list.size(), 1)

    def test_search(self):
        self.linked_list.insert('test')
        node = self.linked_list.search('test')
        self.assertEquals(node.get_data(), 'test')

    def test_delete(self):
        self.linked_list.insert('test')
        self.linked_list.delete('test')
        self.assertEquals(self.linked_list.size(), 0)
