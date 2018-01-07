import unittest

from data_structures.tree import TreeNode, BinarySearchTree


def build_binary_search_tree(keys_values):
    b_tree = BinarySearchTree()
    for key, value in keys_values:
        b_tree.put(key, value)

    return b_tree


class TreeNodeTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_tree_node_instatiate(self):
        right_node = TreeNode(key='test2', value=1)
        left_node = TreeNode(key='test3', value=2)
        tree = TreeNode(key='test', value=0, left_child=left_node,
                        right_child=right_node)
        self.assertEqual(tree.value, 0)
        self.assertEqual(tree.right_child.value, 1)
        self.assertEqual(tree.left_child.value, 2)

    def test_has_right_child(self):
        right_node = TreeNode(key='test2', value=1)
        left_node = TreeNode(key='test3', value=2)
        tree = TreeNode(key='test', value=0, left_child=left_node,
                        right_child=right_node)

        self.assertEqual(tree.has_right_child, True)
    
    def test_has_right_child_false(self):
        left_node = TreeNode(key='test3', value=2)
        tree = TreeNode(key='test', value=0, left_child=left_node,
                        right_child=None)

        self.assertEqual(tree.has_right_child, False)
    
    def test_has_left_child(self):
        left_node = TreeNode(key='test3', value=2)
        tree = TreeNode(key='test', value=0, left_child=left_node,
                        right_child=None)

        self.assertEqual(tree.has_left_child, True)
    
    def test_has_left_child_false(self):
        tree = TreeNode(key='test', value=0, left_child=None,
                        right_child=None)

        self.assertEqual(tree.has_right_child, False)

    def test_is_left_child(self):
        left_node = TreeNode(key='test1', value=1) 
        parent = TreeNode(key='test', value=0, left_child=left_node,
                          right_child=None)
        left_node.parent = parent

        self.assertEqual(left_node.is_left_child, True)

    def test_is_left_child_false(self):
        left_node = TreeNode(key='test1', value=1) 

        self.assertEqual(left_node.is_left_child, False)
    
    def test_is_right_child(self):
        right_node = TreeNode(key='test1', value=1)
        parent = TreeNode(key='test', value=0, left_child=None,
                          right_child=right_node)
        right_node.parent = parent

        self.assertEqual(right_node.is_right_child, True)

    def test_is_right_child_false(self):
        right_node = TreeNode(key='test2', value=1)

        self.assertEqual(right_node.is_right_child, False)
    
    def test_is_root(self):
        tree = TreeNode(key='test1', value=1)

        self.assertEqual(tree.is_root, True)

    def test_is_root_false(self):
        parent = TreeNode(key='test', value=0)
        child = TreeNode(key='test1', value=1, parent=parent)

        self.assertEqual(child.is_root, False)

    def test_is_leaf(self):
        leaf = TreeNode(key='test', value=1)

        self.assertEqual(leaf.is_leaf, True)

    def test_is_leaf_false_left(self):
        child = TreeNode(key='test1', value=1)
        parent = TreeNode(key='test', value=0, left_child=child)

        self.assertEqual(parent.is_leaf, False)

    def test_is_leaf_false_right(self):
        child = TreeNode(key='test1', value=1)
        parent = TreeNode(key='test', value=0, right_child=child)

        self.assertEqual(parent.is_leaf, False)

    def test_has_any_children_right(self):
        right_child = TreeNode(key='test1', value=1)
        parent = TreeNode(key='test', value=0, right_child=right_child)

        self.assertEqual(parent.has_any_children, True)

    def test_has_any_children_left(self):
        left_child = TreeNode(key='test1', value=1)
        parent = TreeNode(key='test', value=0, left_child=left_child)

        self.assertEqual(parent.has_any_children, True)

    def test_has_any_children_both(self):
        right_child = TreeNode(key='test1', value=1)
        left_child = TreeNode(key='test2', value=2)
        parent = TreeNode(key='test', value=0, right_child=right_child,
                          left_child=left_child)

        self.assertEqual(parent.has_any_children, True)

    def test_has_any_children_false(self):
        parent = TreeNode(key='test', value=0)

        self.assertEqual(parent.has_any_children, False)

    def test_has_both_children(self):
        right_child = TreeNode(key='test1', value=1)
        left_child = TreeNode(key='test2', value=2)
        parent = TreeNode(key='test', value=0, right_child=right_child,
                          left_child=left_child)

        self.assertEqual(parent.has_both_children, True)

    def test_has_both_children_both(self):
        parent = TreeNode(key='test', value=0)

        self.assertEqual(parent.has_any_children, False)
    
    def test_replace_node_data_no_children(self):
        tree = TreeNode(key='test', value=0)
        tree.replace_node_data(value=1, key='new_value')

        self.assertEqual(tree.value, 1)
        self.assertEqual(tree.key, 'new_value')
        self.assertEqual(tree.right_child, None)
        self.assertEqual(tree.left_child, None)

    def test_replace_node_data_left_child(self):
        left_child = TreeNode(key='left', value=2)
        tree = TreeNode(key='test', value=0)
        tree.replace_node_data(value=1, key='new_value',
                               left_child=left_child)

        self.assertEqual(tree.value, 1)
        self.assertEqual(tree.key, 'new_value')
        self.assertEqual(tree.left_child, left_child)
        self.assertEqual(tree.right_child, None)
        self.assertEqual(left_child.parent, tree)

    def test_replace_node_data_right_child(self):
        right_child = TreeNode(key='right', value=2)
        tree = TreeNode(key='test', value=0)
        tree.replace_node_data(value=1, key='new_value',
                               right_child=right_child)

        self.assertEqual(tree.value, 1)
        self.assertEqual(tree.key, 'new_value')
        self.assertEqual(tree.right_child, right_child)
        self.assertEqual(tree.left_child, None)
        self.assertEqual(right_child.parent, tree)

    def test_replace_node_data_both_children(self):
        right_child = TreeNode(key='right', value=2)
        left_child = TreeNode(key='left', value=0)
        tree = TreeNode(key='test', value=0)
        tree.replace_node_data(value=1, key='new_value',
                               right_child=right_child,
                               left_child=left_child)

        self.assertEqual(tree.value, 1)
        self.assertEqual(tree.key, 'new_value')
        self.assertEqual(tree.right_child, right_child)
        self.assertEqual(tree.left_child, left_child)
        self.assertEqual(left_child.parent, tree)
        self.assertEqual(right_child.parent, tree)

    def test_find_sucessor_in_right_subtree(self):
        nodes = [(17, 'root'), (5, 'left_1'), (2, 'left_2'), (11, 'right_2'),
                 (9, 'left_3'), (16, 'right_3'), (7, 'left_4'), (8, 'left_5'),
                 (35, 'right_1')]
        tree = build_binary_search_tree(nodes)
        node = tree._get(5, tree.root)
        successor = node.find_successor()
        self.assertEqual(successor.key, 7)
        self.assertEqual(successor.value, 'left_4')

    def test_right_child_has_no_right_child_successor(self):
        nodes = [(17, 'root'), (10, 'left_1'), (35, 'right_1'),
                 (30, 'left_2'), (20, 'left_3'), (33, 'right_3'),
                 (32, 'left_4')]
        tree = build_binary_search_tree(nodes)
        node = tree._get(33, tree.root)
        successor = node.find_successor()
        self.assertEqual(successor.key, 35)
        self.assertEqual(successor.value, 'right_1')

    def test_no_right_child_is_left_child_successor(self):
        nodes = [(17, 'root'), (10, 'left_1'), (35, 'right_1'),
                 (20, 'left_2'), (37, 'left_3'), (42, 'right_2'),
                 (50, 'right_3'), (55, 'right_4')]
        tree = build_binary_search_tree(nodes)
        node = tree._get(37, tree.root)
        successor = node.find_successor()
        self.assertEqual(successor.key, 42)
        self.assertEqual(successor.value, 'right_2')

    def test_find_min_has_left_leaf(self):
        left_node_2 = TreeNode(key='left_node_2', value=-2)
        left_node = TreeNode(key='left_1', value=-1, left_child=left_node_2)
        right_node = TreeNode(key='right_1', value=1)
        root_node = TreeNode(key='root', value=0,
                             right_child=right_node,
                             left_child=left_node)
        right_node.parent = root_node
        left_node.parent = root_node
        left_node_2.parent = left_node

        min_node = root_node.find_min()
        self.assertEqual(min_node, left_node_2)

    def test_find_min_has_no_left_leaf(self):
        right_node = TreeNode(key='right_1', value=1)
        root_node = TreeNode(key='root', value=0,
                             right_child=right_node,
                             left_child=None)
        right_node.parent = root_node

        min_node = root_node.find_min()
        self.assertEqual(min_node, root_node)

    def test_splice_out_is_leaf_left_child(self):
        left_node = TreeNode(key=1, value='left')
        right_node = TreeNode(key=12, value='right')
        parent = TreeNode(key=10, value='root', left_child=left_node,
                          right_child=right_node)
        left_node.parent = parent
        right_node.parent = parent
        left_node.splice_out()
        self.assertEqual(left_node.parent.left_child, None)
        self.assertEqual(right_node.parent.right_child, right_node)

    def test_splice_put_is_leaf_right_child(self):
        right_node = TreeNode(key=12, value='right')
        left_node = TreeNode(key=1, value='left')
        parent = TreeNode(key=10, value='root', right_child=right_node,
                          left_child=left_node)
        right_node.parent = parent
        left_node.parent = parent
        right_node.splice_out()
        self.assertEqual(right_node.parent.right_child, None)
        self.assertEqual(left_node.parent.left_child, left_node)

    def test_splice_out_has_left_child_is_left_child(self):
        left_grandchild = TreeNode(key=-1, value='left_grandchild')
        left_node = TreeNode(key=1, value='left', left_child=left_grandchild)
        parent = TreeNode(key=10, value='root', left_child=left_node)
        left_node.parent = parent
        left_node.splice_out()
        self.assertEqual(parent.left_child, left_grandchild)

    def test_splice_out_has_left_child_is_right_child(self):
        left_grandchild = TreeNode(key=-1, value='left_grandchild')
        right_node = TreeNode(key=1, value='left', left_child=left_grandchild)
        parent = TreeNode(key=10, value='root', right_child=right_node)
        right_node.parent = parent
        right_node.splice_out()
        self.assertEqual(parent.right_child, left_grandchild)

    def test_splice_out_has_left_child(self):
        left_grandchild = TreeNode(key=-1, value='left_grandchild')
        right_node = TreeNode(key=1, value='left', left_child=left_grandchild)
        parent = TreeNode(key=10, value='root', right_child=right_node)
        right_node.parent = parent
        right_node.splice_out()
        self.assertEqual(left_grandchild.parent, parent)
   

    def test_splice_out_has_right_child_is_left_child(self):
        left_grandchild = TreeNode(key=-1, value='left_grandchild')
        right_node = TreeNode(key=1, value='left', left_child=left_grandchild)
        parent = TreeNode(key=10, value='root', right_child=right_node)
        right_node.parent = parent
        right_node.splice_out()
        self.assertEqual(parent.right_child, left_grandchild)

    def test_splice_out_has_right_child_is_right_child(self):
        right_grandchild = TreeNode(key=-1, value='left_grandchild')
        right_node = TreeNode(key=1, value='left', right_child=right_grandchild)
        parent = TreeNode(key=10, value='root', right_child=right_node)
        right_node.parent = parent
        right_node.splice_out()
        self.assertEqual(parent.right_child, right_grandchild)

    def test_splice_out_has_right_child(self):
        right_grandchild = TreeNode(key=-1, value='left_grandchild')
        right_node = TreeNode(key=1, value='left', right_child=right_grandchild)
        parent = TreeNode(key=10, value='root', right_child=right_node)
        right_node.parent = parent
        right_node.splice_out()
        self.assertEqual(right_grandchild.parent, parent)


class BinarySearchTreeTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_put_is_root(self):
        pass

    def test_put_not_root(self):
        pass

    def test__insert_key_greater_than_current_node_left_child(self):
        pass

    def test__insert_key_greater_than_current_node_right_child(self):
        pass

    def test__insert_key_less_than_current_node_right_child(self):
        pass

    def test__insert_key_less_than_current_node_right_child(self):
        pass

    def test_get_is_root(self):
        pass

    def test_is_root_response(self):
        pass

    def test_is_root_response_none(self):
        pass

    def test_is_not_root(self):
        pass

    def test__get_no_current_node(self):
        pass

    def test__get_current_node_key_equal(self):
        pass

    def test__get_current_node_key_greater_than(self):
        pass

    def test__get_all_other_cases(self):
        pass

    def test_delete_size_greater_than_one_node_to_remove(self):
        pass

    def test_delete_size_greater_than_one_no_node_to_remove(self):
        pass

    def test_delete_size_equal_to_one_and_key_is_root(self):
        pass

    def test_delete_size_is_less_than_one(self):
        pass

    def test_remove_is_leaf_parent_has_left_child(self):
        pass

    def test_remove_is_leaf_parent_has_right_child(self):
        pass

    def test_remove_has_both_children(self):
        pass

    def test_remove_has_left_child_is_left_child(self):
        pass

    def test_remove_has_left_child_is_right_child(self):
        pass

    def test_remove_has_left_child_has_not_parent(self):
        pass

    def test_remove_has_right_child_is_right_child(self):
        pass

    def test_remove_has_right_child_is_left_child(self):
        pass

    def test_remove_has_right_child_is_not_parent(self):
        pass
