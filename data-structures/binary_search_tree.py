DEFAULT_K = 3


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.k = DEFAULT_K
        self.size = 1
        return

    def insert(self, newNode):
        # self.size += 1
        print self.value
        inserted = False
        if newNode.value >= self.value + self.k:
            if self.right is None:
                newNode.setParent(self)
                self.right = newNode
                inserted = True
            else:
                inserted = self.right.insert(newNode)
        elif newNode.value <= self.value - self.k:
            if self.left is None:
                newNode.setParent(self)
                self.left = newNode
                inserted = True
            else:
                inserted = self.left.insert(newNode)
        if inserted:
            self.size += 1

        return inserted

    def setParent(self, node):
        self.parent = node
        return

    def findLeftSize(self, value, node=None):
        if node is None:
            node = self
        size = 0
        if node.value <= value:
            size += 1
            if node.left is not None:
                size += node.left.size
            if node.right is not None:
                size += self.findLeftSize(value, node.right)
        else:
            if node.left is not None:
                size += self.findLeftSize(value, node.left)

        return size

        return

    def findmin(self):
        node = self
        while node is not None:
            value = node.value
            node = node.left

        return value

    def findmax(self):
        node = self
        while node is not None:
            value = node.value
            node = node.right

        return value

    def sort(self, node=None, sorted=[]):
        if node is None:
            node = self

        if node.left is not None:
            self.sort(node.left, sorted)

        sorted.append(node.value)

        if node.right is not None:
            self.sort(node.right, sorted)

        return sorted

    def inorder(self):
        node = self
        indent = 1
        stack = []
        stack.append(node)

        print 'inorder walk: ',
        while len(stack) > 0:
            for i in stack:
                print i,
            print ':', node
            left = node.left
            if left is not None:
                stack.append(left)
                node = left
                continue
            node = stack.pop()
            print str(node.value)
            right = node.right
            if right is not None:
                stack.append(right)
                node = right
                continue

        for i in stack:
            print i

    def traverse(self, node=None, indent=1):
        if node is None:
            node = self

        parentInfo = ''
        if node.parent is not None:
            parentInfo = '^' + str(node.parent.value)
        print '..' * indent + \
            str(node.value) + '(' + str(node.size) + ')' + parentInfo
        indent += 1
        if node.left is not None:
            node.traverse(node.left, indent)
        if node.right is not None:
            node.traverse(node.right, indent)

    def __str__(self):
        return str(self.value)


problem = [79, 46, 46, 40, 43, 41, 64, 2, 200, 100, -1, 83, 0]
bst = Node(49)

for i in problem:
    node = Node(i)
    inserted = bst.insert(node)
    if inserted:
        print str(i) + ' is valid'
    else:
        print str(i) + ' is NOT valid'

bst.traverse()
print bst.findmin()
print bst.findmax()
print bst.findLeftSize(55)
# NOT WORKING
print bst.sort()
bst.inorder()
