import unittest

from data_structures.stack import (Stack, 
                                   StackNode)

class StackTest(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push('test')

        self.assertEqual(stack.head.data, 'test')
    
    def test_pop_is_none(self):
        stack = Stack()

        with self.assertRaises(ValueError):
            stack.pop()
    
    def test_pop(self):
        stack = Stack()
        stack.push('win')
        stack.push('test')

        item = stack.pop()

        self.assertEqual(item, 'test')
        self.assertEqual(stack.head.data, 'win')

    def test_peek_is_none(self):
        stack = Stack()

        with self.assertRaises(ValueError):
            stack.peek()

    def test_peek(self):
        stack = Stack()
        stack.push('test')

        self.assertEqual(stack.peek().data, 'test')

    def test_isEmpty(self):
        stack_empty = Stack()
        stack_full = Stack()
        stack_full.push('test')

        self.assertEqual(stack_empty.isEmpty(), True)
        self.assertEquals(stack_full.isEmpty(), False)

