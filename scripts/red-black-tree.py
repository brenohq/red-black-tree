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

    # find the node with the minimum key (leftmost node)
    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    # find the node with the maximum key (rightmost node)
    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

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
        # find the node containing key
        z = self.TNULL
        node = self.root

        while node != self.TNULL:
            if node.key == key:
                z = node

            if node.key <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Couldn't find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == BLACK:
            self.__fix_delete(x)

    # fix the red-black tree modified when insertion occurs
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

    # fix the red-black tree modified when deletion occurs
    def __fix_delete(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == RED:
                    # case x’s sibling S is red
                    s.color = BLACK
                    x.parent.color = RED
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == BLACK and s.right.color == BLACK:
                    # case x’s sibling S is black, and both of S’s children are black
                    s.color = RED
                    x = x.parent
                else:
                    if s.right.color == BLACK:
                        # case x’s sibling S is black, S’s left child is red, and S’s right child is black
                        s.left.color = BLACK
                        s.color = RED
                        self.right_rotate(s)
                        s = x.parent.right

                    # case x’s sibling S is black, and S’s right child is red
                    s.color = x.parent.color
                    x.parent.color = BLACK
                    s.right.color = BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == RED:
                    # case x’s sibling S is red
                    s.color = BLACK
                    x.parent.color = RED
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.left.color == BLACK and s.right.color == BLACK:
                    # case x’s sibling S is black, and both of S’s children are black
                    s.color = RED
                    x = x.parent
                else:
                    if s.left.color == BLACK:
                        # case x’s sibling S is black, S’s left child is red, and S’s right child is black
                        s.right.color = BLACK
                        s.color = RED
                        self.left_rotate(s)
                        s = x.parent.left

                    # case x’s sibling S is black, and S’s right child is red
                    s.color = x.parent.color
                    x.parent.color = BLACK
                    s.left.color = BLACK
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = BLACK

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

    bst.delete(17)

    bst.insert(30)

    bst.print_human_readable_tree()
