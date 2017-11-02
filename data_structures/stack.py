class StackNode(object):

    def __init__(self, prev_node, data):
        self.prev_node = prev_node
        self.data = data

    def next(self):
        return self.prev_node
        

class Stack(object):

    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        """
        Add an item to the top of the stack.
        """
        self.head = StackNode(self.head, data)           

    def pop(self):
        """
        Remove the top item from the stack.
        """
        if self.isEmpty():
            raise ValueError("Stack is empty thus there is no value.")
        else:
            item = self.head.data
            self.head = self.head.next()
            return item

    def peek(self):
        """
        Returns the top of the stack.
        """
        if self.isEmpty():
            raise ValueError("Stack is empty thus there is no value")
        else:
            return self.head

    def isEmpty(self):
        """
        This function determines if there is a head
        node or not.
        """
        return self.head == None

