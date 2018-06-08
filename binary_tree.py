class BinaryTree(object):
    def __init__(self, value):
        self.value = value
        self.left_branch = None
        self.right_branch = None

    def insertLeft(self, value):
        original_left_branch = self.left_branch

        subtree = BinaryTree(value)

        if original_left_branch is not None:
            subtree.left_branch = original_left_branch

        self.left_branch = subtree

    def insertRight(self, value):
        original_right_branch = self.right_branch

        subtree = BinaryTree(value)

        if original_right_branch is not None:
            subtree.right_branch = original_right_branch

        self.right_branch = subtree

    def getRootValue(self):
        return self.value

    def setRootValue(self, value):
        self.value = value

    def getLeftBranch(self):
        return self.left_branch

    def getRightBranch(self):
        return self.right_branch


def preorder(tree):
    if tree is None:
        return

    print(tree.getRootValue())
    preorder(tree.getLeftBranch())
    preorder(tree.getRightBranch())


def inorder(tree):
    if tree is None:
        return

    inorder(tree.getLeftBranch())
    print(tree.getRootValue())
    inorder(tree.getRightBranch())


def postorder(tree):
    if tree is None:
        return

    postorder(tree.getLeftBranch())
    postorder(tree.getRightBranch())
    print(tree.getRootValue())


tree = BinaryTree(1)
tree.insertLeft(3)
tree.insertLeft(2)
tree.insertRight(5)
tree.insertRight(4)

postorder(tree)