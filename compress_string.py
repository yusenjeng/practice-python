

def compress_string(target):
    if not isinstance(target, str):
        raise TypeError('The parameter is not a string.')
    if target == '':
        return ''

    encoded = ''
    counter = 0
    last_char = ''
    for c in target:
        if c != last_char and last_char != '':
            encoded += last_char + str(counter)
            counter = 1
        else:
            counter += 1

        last_char = c

    if last_char != '' and counter > 0:
        encoded += last_char + str(counter)

    return encoded


print( compress_string('') )
print( compress_string('AABBCC') )
print( compress_string('AAABCCDDDDD') )