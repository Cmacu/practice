_BLACK = 'black'
_RED = 'red'
_LEFT = 'left'
_RIGHT = 'right'


class Node:
    def __init__(self, value, color=_RED):
        self.parent = None
        setattr(self, _LEFT, None)
        setattr(self, _RIGHT, None)
        self.value = value
        self.color = _RED

    def __str__(self):
        return str(self.value) + ' (' + self.color + ')'


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, node, current=None):
        if self.root is None:
            self.root = node
            self.root.color = _BLACK
            return True

        if current is None:
            current = self.root

        if current.value > node.value:
            self._insert(node, current, _LEFT)
        else:
            self._insert(node, current, _RIGHT)

        return True

    def _insert(self, node, parent, side):
        current = getattr(parent, side)
        if current is not None:
            return self.insert(node, current)

        node.parent = parent
        setattr(parent, side, node)
        self.fixColors(parent)

    def fixColors(self, node):
        return True

    def delete(self, node):

        return True

    def traverse(self, node=None, indent=1):
        if node is None:
            node = self.root
        print '  ' * (indent - 1), '__', str(node.value)
        indent += 1
        if node.left is not None:
            self.traverse(node.left, indent)
        if node.right is not None:
            self.traverse(node.right, indent)

    def inOrder(self, node=None):
        result = []
        if node is None:
            node = self.root

        if node is None:
            return result

        left = getattr(node, _LEFT)
        if left is not None:
            result.extend(self.inOrder(left))

        result.append(node.value)
        # result.append(node.value)
        right = getattr(node, _RIGHT)
        if right is not None:
            result.extend(self.inOrder(right))

        return result

    def __str__(self):
        return str(self.inOrder(self.root))


problem = [79, 46, 46, 40, 43, 41, 64, 2, 200, 100, -1, 83, 0]
rbTree = RedBlackTree()
for i in problem:
    node = Node(i)
    print node,
    print i, rbTree.insert(node)

rbTree.traverse()
print rbTree
