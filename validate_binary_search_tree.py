class TreeNode(object):
    def __init__(self, key, left_branch=None, right_branch=None, parent=None):
        self.key = key
        self.left_branch = left_branch
        self.right_branch = right_branch
        self.parent = parent


keys = []


def inorder(tree):
    if tree is None:
        return

    if tree.left_branch:
        inorder(tree.left_branch)
    keys.append(tree.key)
    if tree.right_branch:
        inorder(tree.right_branch)


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

n14.right_branch = n13
n13.parent = n14


inorder(n8)
print(keys)