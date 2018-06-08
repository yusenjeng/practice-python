

class TreeNode(object):
    def __init__(self, key, value, left_branch=None, right_branch=None, parent=None):
        self.key = key
        self.value = value
        self.left_branch = left_branch
        self.right_branch = right_branch
        self.parent = parent

    def __iter__(self):
        if self:
            if self.hasLeftBranch():
                for element in self.left_branch:
                    yield element
            yield self.key
            if self.hasRightBranch():
                for element in self.right_branch:
                    yield element

    def __str__(self):
        return "Key={0} Value={1}, LR={2},{3}\r".format(self.key, self.value, self.hasLeftBranch(), self.hasRightBranch())

    def isRoot(self):
        return self.parent is None

    def isLeaf(self):
        return not (self.left_branch or self.right_branch)

    def isLeftBranch(self):
        return self.parent and self.parent.left_branch == self

    def isRightBranch(self):
        return self.parent and self.parent.right_branch == self

    def hasLeftBranch(self):
        return self.left_branch is not None

    def hasRightBranch(self):
        return self.right_branch is not None

    def hasBranch(self):
        return self.left_branch or self.right_branch

    def hasBothBranch(self):
        return self.left_branch and self.right_branch

    def update(self, key, value, left_branch, right_branch):
        self.key = key
        self.value = value
        self.left_branch = left_branch
        self.right_branch = right_branch
        if self.hasLeftBranch():
            self.left_branch.parent = self
        if self.hasRightBranch():
            self.right_branch.parent = self

    def find_min_subtree(self):
        curr_node = self
        while curr_node.hasLeftBranch():
            curr_node = curr_node.left_branch
        return curr_node

    def find_successor(self):
        successor = None
        if self.hasRightBranch():
            successor = self.right_branch.find_min_subtree()
        else:
            if self.parent:
                if self.isLeftBranch():
                    successor = self.parent
                elif self.isRightBranch():
                    self.parent.right_branch = None
                    successor = self.parent.find_successor()
                    self.parent.right_branch = self
        return successor

    def splice_out(self):
        if self.isLeaf():
            if self.isLeftBranch():
                self.parent.left_branch = None
            else:
                self.parent.right_branch = None
        elif self.hasBranch():
            branch = None
            if self.hasLeftBranch():
                branch = self.left_branch
            else:
                branch = self.right_branch

            if self.isLeftBranch():
                self.parent.left_branch = branch
            elif self.isRightBranch():
                self.parent.right_branch = branch
            branch.parent = self.parent


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        return self.find(key)

    def __contains__(self, key):
        return self.find(key) is not None

    def __delitem__(self, key):
        self.delete(key)

    def insert(self, key, value):
        if self.root:
            self.__insert(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def __insert(self, key, value, curr_node):
        if key < curr_node.key:
            if curr_node.hasLeftBranch():
                self.__insert(key, value, curr_node.left_branch)
            else:
                curr_node.left_branch = TreeNode(key, value, parent=curr_node)
        else:
            if curr_node.hasRightBranch():
                self.__insert(key, value, curr_node.right_branch)
            else:
                curr_node.right_branch = TreeNode(key, value, parent=curr_node)

    def find(self, key):
        if self.root:
            node = self.__find(key, self.root)
            if node:
                return node.value
        return None

    def __find(self, key, curr_node):
        if key == curr_node.key:
            return curr_node
        elif key < curr_node.key:
            if curr_node.hasLeftBranch():
                return self.__find(key, curr_node.left_branch)
        else:
            if curr_node.hasRightBranch():
                return self.__find(key, curr_node.right_branch)
        return None

    def delete(self, key):
        if self.size > 1:
            node_to_delete = self.__find(key, self.root)
            if node_to_delete:
                self.__delete(node_to_delete)
                self.size -= 1
                return
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
            return

        raise KeyError(key+' is not found.')

    def __delete(self, node):
        if not node.hasBranch():
            if node.isLeftBranch():
                node.parent.left_branch = None
            elif node.isRightBranch():
                node.parent.right_branch = None
        elif node.hasBothBranch():
            successor = node.find_successor()
            successor.splice_out()
            node.key = successor.key
            node.value = successor.value
        else:
            branch = node.left_branch
            if node.hasRightBranch():
                branch = node.right_branch

            if node.isLeftBranch():
                node.parent.left_branch = branch
                branch.parent = node.parent
            elif node.isRightBranch():
                node.parent.right_branch = branch
                branch.parent = node.parent
            else:
                self.root = branch
                branch.parent = None



if __name__ == '__main__':
    tree = BinarySearchTree()
    tree[3]="red"
    tree[4]="blue"
    tree[6]="yellow"
    tree[2]="at"

    node = tree.root
    print(node)
    print(node.left_branch)
    print(node.right_branch)
    print(node.right_branch.right_branch)

    tree.delete(4)
    node = tree.root
    print(node)
    print(node.left_branch)
    print(node.right_branch)
