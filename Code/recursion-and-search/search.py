#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests

    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively
    # print(f"Runing {index}")
    # print(f"Looking for {item}")
    # print(array[index])

    if index > len(array)-1:
        return None
    elif item == array[index]:
        return index
    return linear_search_recursive(array, item, index + 1)


    # if array[index] == item:
    #     # print(f"First {array[index]}")
    #     return index
    # elif index < len(array)-1:
    #     # index += 1
    #     result = linear_search_recursive(array, item, index + 1)
    # else:
    #     return None

    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests

# ===============================================================================================

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # Got some help, thought I understood, but didn't
    # O(log n)
    low = 0
    high = len(array)-1

    while low <= high:
        # https://www.geeksforgeeks.org/division-operator-in-python/
        mid = (high + low) // 2
        if item > array[mid]:
            low = mid + 1
        elif item < array[mid]:
            high = mid - 1
        else:
            return mid
    return None
    '''

    [1,2,3,4,5,6]
    num is 5
    low = 0
    high = 5

    ----
    1st
    mid = 2
    if 5 > 3:
        low = 2

    2nd
    low = 2
    high = 5
    mid = 3

    if 5 > 4:
        low = 3

    3rd
    low = 3
    high = 5
    mid = (5+3)//2 = 4

    if 5 > 5:
    if 5 < 5:
    else:
        return 4???

    but low nor high changes then, so thats why its mid +1 or -1

    num is 5
    low = 0
    hight = 5

    1st mid = 2
    if 5 > 3:
        low = 2 +1

    2nd
    low = 3
    high = 5
    mid = 4
    if 5 > 5
    if 5 < 5
    else:
    return 4???
    '''


# binary_search_recursive(array, item, left=None, right=None) Originally
def binary_search_recursive(array, item, low=None, high=None):
    # TODO: implement binary search recursively here

    if low == None and high == None:
        ''' Making sure not to overide future calls where low and high are passed'''
        low = 0
        high = len(array)-1

    if low > high:
        ''' If item isn't in the list'''
        return None

    mid = (high + low) // 2

    if item > array[mid]:
        ''' If item higher than mid'''
        return binary_search_recursive(array, item, mid + 1, high)
    elif item < array[mid]:
        ''' If item lower than mid '''
        return binary_search_recursive(array, item, low, mid - 1)
    else:
        return mid

    # return binary_search_recursive(array, item, low, high)


    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
