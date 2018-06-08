from stack import *

stack = Stack()

mapping = {')': '(', ']': '[', '}': '{'}

valid_chars = set()
valid_chars.add('(')
valid_chars.add('[')
valid_chars.add('{')


def balance_check(symbols):
    stack = Stack()

    for char in symbols:
        if char in valid_chars:
            stack.push(char)
        else:
            if mapping[char] == stack.peek():
                stack.pop()
            else:
                return False

    return True


print(balance_check('[]'))
print(balance_check('[()]'))
print(balance_check('[)]'))
print(balance_check('()(){]}'))
print(balance_check(''))
