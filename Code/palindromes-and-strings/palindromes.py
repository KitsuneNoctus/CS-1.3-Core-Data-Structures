#!python

import string
from string import punctuation
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    text = text.lower()
    new_text = ''
    for char in text:
        if char in string.ascii_lowercase:
            new_text += char
    print(new_text)

    reverse = new_text[::-1]
    if new_text == reverse:
        return True
    return False

    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    if text == '':
        return True
    text = text.lower()
    reverse = text[::-1]

    l_char = ''
    r_char = ''

    ''' Third attempt '''
    if left == None and right == None:
        left = 0
        right = 0
        l_char = text[left]
        r_char = reverse[right]
    else:
        if left <= len(text)-1 and right <= len(reverse)-1:
            l_char = text[left]
            r_char = reverse[right]
        elif left == right:
            return True

    if l_char not in string.ascii_lowercase:
        print("Left not in")
        is_palindrome_recursive(text, left + 1, right)

    if r_char not in string.ascii_lowercase:
        print("Right not in")
        is_palindrome_recursive(text, left, right + 1)

    if l_char == r_char:
        return is_palindrome_recursive(text, left + 1, right + 1)
    return False

    ''' Second Attempt Thoughts '''
    # if left == None and right == None:
    #     print("Starting...")
    #     left = text[0]
    #     print(f"Left: {left}")
    #     right = text[len(text)-1]
    #     print(f"Right: {right}")
    #
    # if left not in string.ascii_lowercase:
    #     print("Left not in")
    #     is_palindrome_recursive(text, left + 1, right)
    #
    # if right not in string.ascii_lowercase:
    #     print("Right not in")
    #     is_palindrome_recursive(text, left, right - 1)
    #
    # if left == right:
    #     return

    ''' First attempt thoughts'''
    # if text.index(right) == text.index(left):
    #     return True

    # if
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
    # is_palindrome("tacocat")
    # is_palindrome("deed")

    # is_palindrome("taco cat")
    # is_palindrome("Taco cat")
    # is_palindrome("taco' cat")


    # print(is_palindrome_recursive("IllicitT"))
    # print(is_palindrome_recursive("tacocat"))
