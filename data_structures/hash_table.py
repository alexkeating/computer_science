class Item(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'<Item key={self.key} value={self.value}>'


class HashTable(object):

    def __init__(self, size=0):
        self.size = size
        self.table = [[] for slot in range(0, self.size)]
    
    def __repr__(self):
        return f'<HashTable size={self.size}>'

    def _hash_function(self, data):
        sum = 0

        for index, char in enumerate(data):
            sum += ord(char) + index

        return sum

    def set(self, key, value):
        index = self._hash_function(key) % self.size
        item = self.table[index]
        new_item = Item(key, value)

        if not item:
            self.table[index] = [new_item]
        else:
            self.table[index].append(new_item)

        return f'Inserted value={value} with key={key}'

    def get(self, key):
        index = self._hash_function(key) % self.size
        items = self.table[index]
        if not items:
            raise ValueError(f'Value{key} not in HashTable')
        for item in items:
            if item.key == key:
                return item.value
        raise ValueError(f'Value={key} not in HashTable')

    def remove(self, key):
        index = self._hash_function(key) % self.size
        items = self.table[index]

        for item_index, item in enumerate(items):
            if item.key == key:
                items.remove(item)
                return f'Item with key={item.key} and value={item.value}'
        raise ValueError(f'Value={key} not in HashTable')
