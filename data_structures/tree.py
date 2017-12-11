class TreeNode(object):

    def __init__(self, data, children=None):
        self.data = data
        self.children = children

    def __repr__(self):
        return f'<TreeNode {self.data}>'
