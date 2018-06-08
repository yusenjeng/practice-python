


def word_split(target, words):

    for i in range(len(target)+1):
        if target[0:i] in words:
            print( target[0:i], target[i:] )
            return [target[0:i]] + word_split(target[i:], words)

    return []


if __name__ == '__main__':
    print( word_split('ilovedogsJohn', ['i', 'am', 'a', 'lover', 'love', 'dogs', 'John']) )