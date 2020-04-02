#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    digits = digits[::-1]
    base_ten_conversion = 0
    strings = string.digits + string.ascii_uppercase

    for i, num in enumerate(digits):
        print(f"i: {i}, num: {num}")
        print(base**i)
        print(strings.index(num))
        base_ten_conversion += (base**i) * strings.index(num)
        # base_ten_conversion += num * (base**i)

    # TODO: Decode digits from binary (base 2)
    # if base == 2:
    #     print("base 2")
    #     # for i in len(digits)-1:
    #     #     print(i)
    #     #     num = int(reverse_digits[i])
    #     #     convert = num * (base ** i)
    #     #     base_ten_conversion += convert
    #
    # # TODO: Decode digits from hexadecimal (base 16)
    # elif base == 16:
    #     print("Base 16")
    #
    # # TODO: Decode digits from any base (2 up to 36)
    # else:
    #     print("Other base")

    return base_ten_conversion


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    converting = True

    if base == 2:
        base_two_number = ''
        while(converting):
            base_two_number += str(number % 2)
            number = number / 2
            if number <= 1:
                converting = False

        return base_two_number
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    if base1 == '2' and base2 == '16':
        print("Converting base 2 to base 16")
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    elif base1 == '2' and base2 == '10':
        print("Converting base 2 to base 10")
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    elif base1 == '10' and base2 == '16':
        print("Converting base 10 to base 16")
    # TODO: Convert digits from any base to any base (2 up to 36)
    else:
        print("Converting any bases")


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
