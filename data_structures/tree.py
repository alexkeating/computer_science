class TreeNode(object):

    def __init__(self, key, value, left_child=None, right_child=None, parent=None):
        self.value = value
        self.key = key
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def __repr__(self):
        return f'<TreeNode key={self.key} value={self.value}>'
    
    @property
    def has_right_child(self):
        return self.right_child is not None
    
    @property
    def has_left_child(self):
        return self.left_child is not None

    @property
    def is_left_child(self):
        return self.parent is not None and self.parent.left_child == self

    @property
    def is_right_child(self):
        return self.parent is not None and self.parent.right_child == self

    @property
    def is_root(self):
        return not self.parent

    @property
    def is_leaf(self):
        return not self.has_any_children

    @property
    def has_any_children(self):
        return self.has_left_child or self.has_right_child

    @property
    def has_both_children(self):
        return self.has_left_child and self.has_right_child

    def replace_node_data(self, value, key, left_child=None, right_child=None):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

        if self.has_left_child:
            self.left_child.parent = self
        if self.has_right_child:
            self.right_child.parent = self

    def find_successor(self):
        successor = None
        if self.has_right_child:
            successor = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child:
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_cild = self
        return successor

    def find_min(self):
        current = self
        while current.has_left_child:
            current = current.left_child
        return current

    def splice_out(self):
        """
        Removes successor node.
        """
        if self.is_leaf:
            if self.is_left_child:
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children:
            if self.has_left_child:
                if self.is_left_child:
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child:
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent


class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key, value):
        self.get(key)

    def __contains__(self, key):
        has_key = self.get(key)
        if has_key:
            return True
        else:
            return False

    def __delitem__(self, key):
        self.delete(key)

    def put(self, key, value):
        if self.root:
            self._insert(self.root, key, value)
        else:
            self.root = TreeNode(key, value)

    def _insert(self, current_node, key, value):
        """
        Does not handle duplicate keys.
        """
        if key < current_node.key:
            if current_node.has_left_child:
                self._insert(current_node.left_child, key, value)
            else:
                current_node.left_child = TreeNode(key=key, value=value, parent=current_node)
        else:
            if current_node.has_right_child:
                self._insert(current_node.right_child, key, value)
            else:
                current_node.right_child = TreeNode(key=key, value=value, parent=current_node)

    def get(self, key):
        if self.root:
            response = self._get(key, self.root)
            if response:
                return response.value
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self.get(key)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError("KeyError: Key not in BinaryTree unable to delete.")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("KeyError: Key not in BinaryTree unable to delete.")
    
    def remove(current_node):
        if current_node.is_leaf:
            if current_node == current_node.parent.has_left_child:
                current_node.parent.has_left_child = None
            else:
                current_node.parent.has_right_child = None
        elif current_node.has_both_children:
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.key = successor.key
            current_node.value = successor.value
        else:
            if current_node.has_left_child:
                if current_node.is_left_child:
                    current_node.left_child.parent == current_node.parent
                elif current_node.is_right_child:
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_node_data(current_node.left_child.value,
                                                   current_node.left_child.key,
                                                   current_node.left_child.left_child,
                                                   current_node.left_child.right_child)
            else:
                if current_node.is_right_child:
                    current_node.right_child.parent == current_node.parent
                elif current_node.is_left_child:
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.value,
                                                   current_node.right_child.key,
                                                   current_node.right_child.left_child,
                                                   current_node.right_child.left_child)



