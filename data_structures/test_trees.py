import unittest

from data_structures.tree import TreeNode


class TreeNodeTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_tree_node_instatiate(self):
        tree = TreeNode(data='test', children=[TreeNode(data='test2'),
                                               TreeNode(data='test3')])
        self.assertEqual(tree.data, 'test')
        self.assertEqual(tree.children[0].data, 'test2')
        self.assertEqual(tree.children[1].data, 'test3')
