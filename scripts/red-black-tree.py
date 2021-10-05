import sys

RED = 'red'
BLACK = 'black'


class Node():
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = RED


class RedBlackTree():
    # init the tree with a empty black node as root node
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = BLACK
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    # rotate left at node x
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):

        node = Node(key)
        node.left = self.TNULL
        node.right = self.TNULL

        y = None
        x = self.root

        # interating the tree searching for the correct leaf node to do the insertion
        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        # if new node is a root node, simply return
        if node.parent == None:
            node.color = BLACK
            return

        # if the grandparent is None, simply return
        if node.parent.parent == None:
            return

        # Rebalance the tree after an insertion
        self.__fix_insert(node)

    def delete(self, key):
        return True

    # fix the red-black tree
    def __fix_insert(self, k):
        while k.parent.color == RED:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # uncle
                if u.color == RED:
                    # P is red and U is red too
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # P is right child of G and K is left child of P
                        k = k.parent
                        self.right_rotate(k)
                    # P is right child of G and K is right child of P
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # uncle

                if u.color == RED:
                    # P is red and U is red too.
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # P is right child of G and K is left child of P
                        k = k.parent
                        self.left_rotate(k)
                    # P is right child of G and K is right child of P
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = BLACK

    def print_human_readable_tree(self):
        self.__print_helper(self.root, "", True)

    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            print(str(node.key) + "(" + node.color.upper() + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)


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
    bst.insert(27)
    bst.insert(82)
    bst.insert(13)
    bst.delete(27)
    bst.insert(1)
    bst.insert(6)

    bst.print_human_readable_tree()
