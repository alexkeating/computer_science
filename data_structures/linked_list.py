
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return f'<Node data={self.data}>'

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return f'<LinkedList head={self.head}>'

    def insert(self, data):
        new_node = Node(data=data)
        new_node.set_next_node(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next_node()
        return count

    def search(self, data):
        current = self.head
        found = False

        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next_node()

        if not current:
            raise ValueError('Value not in linked list')
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False

        while current and found:
            if current.get_data() == data:
                previous.set_ext_node = current
                found = True
            else:
                previous = current
                current = current.get_next_node()

        if not current:
            raise ValueError('Value not in list')
        if not previous:
            self.head = current.get_next_node()
        return f'Value: {data} was deleted'
