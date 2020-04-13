#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)

    if pattern in text:
        return True
    return False

    # pattern_length = len(pattern)
    # count = 0
    # for char in text:
    #     if count == pattern_length:
    #         return True
    #     if char == pattern[count]:
    #         count += 1
    #     else:
    #         count = 0
    # return False

    # if pattern == '':
    #     return True
    '''
    def find index():

        or ---
        l = find_mult_index(array, pattern, 1)
        if len(l) > 0:
            return l[0]
        else:
            return None
        ---

        loop (i): 0 --> len(text) - len(pattern)
            #strictly
            #for/else statement - else only runs if break doesn't happen and full for loop runs
            loop(j): 0 -> len(pattern) - 1
                if text[i+j] != pattern[j]
                    break #ONly out of this inner loop
                else
                    return i

    '''


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # if pattern == '':
    #     return 0

    l = find_all_indexes(text, pattern, 1)
    print("----")
    if len(l) > 0:
        return l[0]
    else:
        return None

    # compare_limit = len(text) - len(pattern)
    # pattern_length = len(pattern) - 1
    #
    # for i in range(0, compare_limit):
    #     for j in range(0, pattern_length):
    #         if text[i + j] != pattern[j]:
    #             break
    #
    #     else:
    #         return i
    # return None


    # TODO: Implement find_index here (iteratively and/or recursively)
    # if contains(text,pattern) == True:
    #     for i in range(0, len(text)-1):
    #         print(text[i])
    #         if text[i] == pattern[0]:
    #             print("Tru")
    #             print(text[i:len(pattern)-1])
    #             if text[i:len(pattern)] == pattern:
    #                 return i
    # return None


    '''
    def find_mult_index(array, pattern, flag=0):
        list = []
        loop (i): 0 --> len(text) - len(pattern)
            #strictly
            #for/else statement - else only runs if break doesn't happen and full for loop runs
            loop(j): 0 -> len(pattern) - 1
                if text[i+j] != pattern[j]
                    break #ONly out of this inner loop
                else
                    return list.append(i)
                    #if using a flag
                    if flag == 1:
                        return list
        return list

    '''


def find_all_indexes(text, pattern, flag=0):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    if len(pattern) <= 0:
        compare_limit = len(text) - 1
        pattern_length = len(pattern)
    else:
        compare_limit = len(text) - len(pattern)
        pattern_length = len(pattern) - 1

    list = []
    print(f"Comparing - {pattern} in {text}")
    print(f"Compare limit: {compare_limit}")

    for i in range(0, compare_limit+1):
        print(i)
        #Check through the entire text to maximum before error
        print(f"Pattern Length: {pattern_length}")
        if pattern_length == 0:
            if pattern == '':
                list.append(i)
            elif text[i] != pattern[0]:
                print("Nope")
            else:
                list.append(i)

            if flag == 1:
                list.append(i)
                return list
        else:
            for j in range(0, pattern_length):
                print(f"Text: {text[i+j]} - Pattern {pattern[j]}")
                if text[i+j] != pattern[j]:
                    print("Break")
                    break
            else:
                if flag == 1:
                    list.append(i)
                    return list
                list.append(i)
    return list

    # list = []
    # for i in range(0, compare_limit):
    #     for j in range(0, pattern_length):
    #         if text[i + j] != pattern[j]:
    #             break
    #
    #     else:
    #         if flag == 1:
    #             return list
    #         list.append(i)
    # return list


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()

    # print(find_all_indexes("hahahaha", "ha"))
    # print("---------")
    # print(find_all_indexes("abc", "z"))
    # print(find_all_indexes("abc", "a"))
    # print("---------")


    # print(find_all_indexes("abc", ""))
    # print("-------")
    # print(find_index("abc", ""))


    # print("---------")
    # print(find_all_indexes("abcawser", "z"))
    # print("---------")
    # print(find_index("happy","ha"))
    # print("--------")
    # print(find_index("pphay","ha"))
