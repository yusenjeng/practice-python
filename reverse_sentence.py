
def reverse_sentence_cheat(sentence):

    tokens = sentence.split(' ')
    tokens.reverse()
    return ''.join([x+' ' for x in tokens if x != ''])


def reverse_sentence(sentence):
        if len(sentence) < 1:
            return ''
        if sentence == '':
            return ''

        sentence = sentence.strip(' ')

        reversed_words = []
        head = 0
        tail = 1
        while tail <= len(sentence):
            if tail == len(sentence):
                    reversed_words.insert(0, sentence[head:tail])
                    break

            if sentence[tail] == ' ':
                 if  sentence[tail-1] ==  ' ':
                    head += 1
                 else:
                    reversed_words.insert(0, sentence[head:tail])
                    tail += 1
                    head = tail
            tail += 1

        return ''.join([x+' ' for x in reversed_words])


print( reverse_sentence('hi john,    are you ready to go?') )
print( reverse_sentence('    space before') )