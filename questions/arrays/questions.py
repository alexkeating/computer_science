def string_is_unique(string):
    """
    Question 1: Implement an algoithm to determine if a string has all unique
    characters. What if you cannot use additional data structures.

    Big O:
        Time: O(n)
        Space: O(1)

    Possible solution in python is to use a set and compare the length of
    the set to the length of the original string.
    """
    unique_char = []
    for char in string:
        if char in unique_char:
            return False
        unique_char.append(char)
    return True


def check_permutations(s_one, s_two):
    """
    Question 2: Given two strings, write a method to decide if one is a permutation
    of the other.
    """
    if len(s_one) != len(s_two):
        return False

    h_table = {}
    for index, char in enumerate(s_two):
        h_table[char] = index

    for char in set(s_one):
        if char not in list(h_table.keys()):
            return False
        del h_table[char]
    return True


def urlify(string, length):
    """
    Question 3: Write a method to replace all spaces in a string with '%20'. You may
    assume that the string has suffcient space at the end to hold the additional characters,
    and that you are given the "true" length of the string.

    In python I can use the replace method. string.replace(' ', '%20')
    """
    if not length:
        return None

    chars = []
    last_char = None
    for index, char in enumerate(string):
        if not index <= length:
            continue
        if last_char == '%20' and char == ' ':
            continue
        if char == ' ':
            char = '%20'
        last_char = char
        chars.append(char)
    return ''.join(chars)


def palindrome_permutation(string):
    """
   Question 4: Given a string, write a function to check if it is a permutation of a palindrome.
   A palindrome is a word or phrase that is the same forwards and backwords. A permutation is
   a rearrangement of letters. The palindrome does not need to be limited to a dictionary of
   words.
   """
    pass
