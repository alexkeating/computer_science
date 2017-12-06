import unittest

from questions.stacks_queues.questions import StackMin, DataIntegrityException


def insert_values(stack, iterable):
    for value in iterable:
        stack.push(value)
    return stack


class StackAndQueuesTestCase(unittest.TestCase):

    def setUp(self):
        self.stack_min = StackMin()

    def test_stack_min_normal(self):
        values = (4, 3, 2, 1)
        insert_values(self.stack_min, values)
        min_ = self.stack_min.min()
        self.assertEqual(min_, 1)

    def test_stack_min_insert_greater_value(self):
        values = (4, 3, 2, 1, 2)
        with self.assertRaises(DataIntegrityException):
            insert_values(self.stack_min, values)
