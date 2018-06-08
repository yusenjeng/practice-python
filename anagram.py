def anagram(str1, str2):
    if not isinstance(str1, str):
        raise TypeError('Parameter 1 is needed to be a string.')
    if not isinstance(str2, str):
        raise TypeError('Parameter 2 is needed to be a string.')
    if len(str1) <= 0 or len(str2) <= 0:
        raise ValueError('Parameters can not be empty strings.')

    str1 = str1.lower().replace(' ', '')
    str2 = str2.lower().replace(' ', '')

    char_buckets = {}

    # count the occurrence of each characters in str1
    for char in str1:
        if char in char_buckets:
            char_buckets[char] += 1
        else:
            char_buckets[char] = 1

    # count the occurrence of each characters in str2
    for char in str2:
        if char in char_buckets:
            char_buckets[char] -= 1
        else:
            return False

    for char in char_buckets:
        if char_buckets[char] != 0:
            return False

    return True


# print( anagram('aab', 'baa') )
# print( anagram('go go go', 'gggooo') )
# print( anagram('hi man', 'hi     man') )
# print( anagram('aabbcc', 'aabbc') )
# print( anagram('123', '1 2') )
print(anagram('aab', 'bab'))


def anagram_better(str1, str2):
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError('Parameters are needed to be string type.')

    if len(str1) <= 0 or len(str2) <= 0:
        raise ValueError('Parameters can not be empty strings.')

    str1 = str1.lower().replace(' ', '')
    str2 = str2.lower().replace(' ', '')

    print(str1, str2)
    summed_value = 0
    for char in str1:
        summed_value += ord(char)

    for char in str2:
        summed_value -= ord(char)

    return (summed_value == 0)


# print('======')
# print( anagram_better('aab', 'baa') )
# print( anagram_better('go go go', 'gggooo') )
# print( anagram_better('hi man', 'hi     man') )
# print( anagram_better('aabbcc', 'aabbc') )
# print( anagram_better('123', '1 2') )
print(anagram_better('aab', 'baa'))
