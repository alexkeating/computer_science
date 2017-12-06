from data_structures.stack import Stack, StackNode


def three_in_one():
    """
    Describe how you could use a single array to implement 3 stacks.
    """
    pass


class StackMin(Stack):
    """
    This stack has a min function and return the min
    in O(1) time.
    """
    def __init__(self, head=None):
        super().__init__(head)
        self.min_ = None

    def push(self, data):
        if self.min_ is None or data < self.min_:
            self.head = StackNode(self.head, data)
            self.min_ = self.head.data
        else:
            raise DataIntegrityException('Value was higher than the minimum value in'
                                         'the stack')

    def pop(self):
        if self.isEmpty():
            raise ValueError("Stack is empty thus there is no value.")
        else:
            item = self.head.data
            self.head = self.head.next()
            self.min_ = self.head.data
            return item

    def min(self):
        return self.min_


class DataIntegrityException(Exception):
    pass


def stack_min(stack_min):
    """
    How would you design a stack which, in addition to push and pop,
    has a function min which returns the minimum elelement. Push, pop
    and min should alloperate in O(1) time.

    I would design the push to throw an error if a smaller number is added
    to the stack.
    """
    return stack_min.min()
