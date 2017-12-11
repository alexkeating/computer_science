from copy import deepcopy

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


class SetOfStacks(object):
    """
    Imagine a (literal) stack of plates. If the stack gets too high, it might
    topple. Therefore in real life, we would likely start a new stack when the
    previous stack exceeds some threshold. Implement a data structure SetOfStacks
    that mimics this. SetOfStacks should be composed of several stacks and should
    create a new stack one the previous one exceeds capacity. SetOfStacks.push()
    and SetOfStacks.pop() should behave identically to a single stack.
    """

    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.list_of_stacks = []
        self.head_stack = Stack()
        self.head_stack_size = 0

    def push(self, data):
        if self.stack_size < self.stack_size:
            self.head_stack.push(data)
        else:
            head_copy = deepcopy(self.head_stack)
            self.list_of_stacks.append(head_copy)
            self.head_stack = Stack().push(data)

    def pop(self):
        if self.head_stack.head:
            data = self.head_stack.head.data
            self.head_stack.head = None
            return data
        else:
            self.head_stack = self.list_of_stacks[-1]
            data = self.head_stack.head.data if self.head_stack.head else None
            if not self.head_stack.head:
                raise ValueError('No value to pop')
            self.head_stack.head = None
            return data
