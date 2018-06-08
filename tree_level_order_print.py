class TreeNode(object):
    def __init__(self, key, left_branch=None, right_branch=None, parent=None):
        self.key = key
        self.left_branch = left_branch
        self.right_branch = right_branch
        self.parent = parent


n1 = TreeNode(1)
n3 = TreeNode(3)
n4 = TreeNode(4)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
n10 = TreeNode(10)
n13 = TreeNode(13)
n14 = TreeNode(14)

n8.left_branch = n3
n8.right_branch = n10
n3.parent = n8
n10.parent = n8

n3.left_branch = n1
n3.right_branch = n6
n1.parent = n3
n6.parent = n3

n1.parent = n3

n6.left_branch = n4
n6.right_branch = n7
n4.parent = n6
n7.parent = n6

n10.right_branch = n14
n14.parent = n10

n14.left_branch = n13
n13.parent = n14


def bfs(tree):
    if tree is None:
        return

    que = [(tree, 1)]

    prev_level = 0

    result = ''

    while len(que) > 0:
        node, level = que.pop(0)

        if level != prev_level:
            print(result)
            result = ''
            prev_level = level

        result += str(node.key) + ' '

        if node.left_branch:
            que.append((node.left_branch, level + 1))

        if node.right_branch:
            que.append((node.right_branch, level + 1))

    print(result)


bfs(n8)