import unittest

from data_structures.hash_table import HashTable


class HashTableTest(unittest.TestCase):

    def setUp(self):
        self.hash_table = HashTable(8)

    def test_hash_function(self):
        hash_value = self.hash_table._hash_function('abc')
        self.assertEquals(hash_value, 297)

    def test_set_and_set(self):
        self.hash_table.set('key', 'value')
        value = self.hash_table.get('key')
        self.assertEquals(value, 'value')

    def test_remove(self):
        self.hash_table.set('key', 'value')
        self.hash_table.remove('key')
        with self.assertRaises(ValueError):
            self.hash_table.get('key')
