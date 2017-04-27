# TODO: Add some sort of benchmarks
array_of_numbers = [4, 6, 1, 0]


def merge(right, left, output=list()):
    """
    This function merges two sorted lists.

    :param right: 
    :param left: 
    :param output: 
    :return: 
    """
    if not right and not left:
        return output

    if left:
        left_min = min(left)
    else:
        left_min = min(right) + 1
    if right:
        right_min = min(right)
    else:
        right_min = left_min + 1

    if left_min > right_min:
        right.remove(right_min)
        output.append(right_min)
    elif right_min > left_min:
        left.remove(left_min)
        output.append(left_min)
    elif right_min == left_min:
        right.remove(right_min)
        left.remove(left_min)
        output.append(left_min)
        output.append(right_min)

    return merge(right, left, output)


def merge_sort(array_of_numbers):
    """
    This should split the array into single numbers and then recombine
    the list into a single sorted list in a recursive way.
    
    :param array_of_numbers: 
    :return: 
    """
    length = len(array_of_numbers)
    split = int(length/2)

    if length <= 1:
        return array_of_numbers

    left = merge_sort(array_of_numbers[:split])
    right = merge_sort(array_of_numbers[split:])

    return merge(right, left, output=[])


if __name__ == '__main__':
    sorted_ = merge_sort(array_of_numbers)
    print(sorted_)
