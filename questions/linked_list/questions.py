def remove_dups(linked_list):
    """
    Write code to remove duplicates from an unsorted linked list.
    How would you solve this problem if a temporary buffer is not
    allowed?
    """
    done = False
    list_ = linked_list
    node = list_.head
    while done is False:
        if not node:
            done = True
        else:
            new_node = list_.search(node.data)
            if new_node != node:
                list_.delete(node.data)
            node = node.get_next_node()
    return list_


def return_kth_to_last(linked_list):
    """
    Implement an algorithm to find the kth to last element in a
    singly linked list.
    """
    pass


def delete_middle_node(linked_list, node):
    """
    Implement an algorithm to delete a node in the middle (i.e., any
    node but the and last node not necessarily the exact middle) of
    a singly linked list, given only access to that node.
    """
    pass
