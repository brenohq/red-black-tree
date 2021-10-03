class Node():
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = 'red'


class RedBlackTree():
    def __init__(self):
        self.ROOT_NODE = Node(0)
        self.ROOT_NODE.color = 'black'
        self.ROOT_NODE.left = None
        self.ROOT_NODE.right = None
        self.root = self.ROOT_NODE

    def left_rotate(self, node):
        return True

    def right_rotate(self, node):
        return True

    def insert(self, key):
        return True

    def delete(self, key):
        return True

    def print_human_readable_tree(self):
        print('human readable tree')


if __name__ == "__main__":
    bst = RedBlackTree()

    bst.insert(8)
    bst.insert(18)
    bst.insert(5)
    bst.insert(15)
    bst.insert(17)
    bst.insert(25)
    bst.insert(40)
    bst.insert(80)
    bst.delete(25)

    bst.print_human_readable_tree()
