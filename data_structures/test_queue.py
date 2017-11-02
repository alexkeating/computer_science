import unittest

from data_structures.queue import (Queue,
                                   QueueNode)

class Queuetest(unittest.TestCase):

    def test_add_one(self):
       queue = Queue()
       queue.add('test')

       self.assertEqual(queue.first.data, 'test')
       self.assertEqual(queue.last.data, 'test')

    def test_add_two(self):
        queue = Queue()
        queue.add('keating')
        queue.add('test')

        self.assertEqual(queue.first.data, 'keating')
        self.assertEqual(queue.last.data, 'test')
    
    def test_remove_empty(self):
        queue = Queue()
        
        with self.assertRaises(ValueError):
            queue.remove()

    def test_remove(self):
        queue = Queue()
        queue.add('one')
        queue.add('two')
        
        data = queue.remove()
        
        self.assertEqual(data, 'one')
        self.assertEqual(queue.first.data, 'two')
        self.assertEqual(queue.last.data, 'two')

    def test_peek_empty(self):
        queue = Queue()
        with self.assertRaises(ValueError):
            queue.peek()

    def test_peek(self):
       queue = Queue()
       queue.add('test')
       queue.add('win')

       self.assertEqual(queue.peek(), 'test')

    def test_isEmpty_true(self):
        queue = Queue()
        
        self.assertEqual(queue.isEmpty(), True)

    def test_isEmpty_false(self):
       queue = Queue()
       queue.add('test')

       self.assertEqual(queue.isEmpty(), False)

