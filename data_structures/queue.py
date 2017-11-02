class QueueNode(object):

    def __init__(self, next_node, prev_node,
                 data):
        self.next_node = next_node
        self.prev_node = prev_node
        self.data = data


class Queue(object):

    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last

    def add(self, data):
        """
        Add an item to the end of the list.
        """
        if not self.last:
            self.last = QueueNode(self.first, None, data)
        else:
            old_node = self.last
            self.last = QueueNode(old_node, None, data)
            old_node.prev_node = self.last
        if not self.first:
            self.first = self.last

    
    def remove(self):
       """
       Remove the first item in the queue.
       """
       if self.isEmpty():
           raise ValueError("Queue is empty cannot remove item")
       else:
           item_data = self.first.data
           self.first = self.first.prev_node
           if not self.first:
               self.last = None
           return item_data

    def peek(self):
        """
        Return the top of the queue.
        """
        if self.isEmpty():
            raise ValueError("Queue is empty cannont peek.")
        else:
            return self.first.data

    def isEmpty(self):
        """
        Returns True if and only if the queue is
        empty.
        """
        return self.first == None

