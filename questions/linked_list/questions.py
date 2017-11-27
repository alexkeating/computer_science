def remove_dups(linked_list):
    """
    Write code to remove duplicates from an unsorted linked list.
    How would you solve this problem if a temporary buffer is not
    allowed?

    O(N^2) - with no buffer
    O(N) with buffer
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
    if not linked_list:
        return None

    values = {}
    pass_ = 0
    node = linked_list.head
    done = False
    while done is False:
        if not node:
            kth = values.get(pass_ - 1 if pass_ != 1 else 1)
            return kth
        else:
            pass_ += 1
            values[pass_] = node
            node = node.get_next_node()


def delete_middle_node(linked_list, node):
    """
    Implement an algorithm to delete a node in the middle (i.e., any
    node but the and last node not necessarily the exact middle) of
    a singly linked list, given only access to that node.
    """
    pass
