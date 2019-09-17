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

    def findmin(self, node=None):
        if node is None:
            node = self
        while node.left is not None:
            node = node.left

        return node

    def findmax(self, node=None):
        if node is None:
            node = self
        while node.right is not None:
            node = node.right

        return node

    def sort(self, node=None, sorted=[]):
        if node is None:
            node = self

        if node.left is not None:
            self.sort(node.left, sorted)

        sorted.append(node.value)

        if node.right is not None:
            self.sort(node.right, sorted)

        return sorted

    def successor(self, node=None):
        if node is None:
            node = self

        if node.right is not None:
            return self.findmin(node.right)
        parent = node.parent
        while parent is not None and node == parent.right:
            node = parent
            parent = node.parent

        return parent

    def predecessor(self, node=None):
        if node is None:
            node = self

        if node.left is not None:
            return self.findmax(node.left)
        parent = node.parent
        while node.parent is not None and node == parent.left:
            node = parent
            parent = node.parent

        return parent

    def inOrder(self):
        node = self
        result = []

        while node is not None:
            if node.left is None:
                result.append(node.value)
                node = node.right
            else:
                # Find the inorder predecessor of current
                pre = node.left
                while(pre.right is not None and pre.right != node):
                    pre = pre.right

                # Make current as right child of its inorder predecessor
                if(pre.right is None):
                    pre.right = node
                    node = node.left

                # Revert the changes made in if part to restore the
                # original tree i.e., fix the right child of predecessor
                else:
                    pre.right = None
                    result.append(node.value)
                    node = node.right

        return result

    def inOrder_stack(self):
        result = []
        stack = []
        node = self

        while True:
            if node is not None:
                stack.append(node)
                node = node.left
                continue
            if len(stack):
                node = stack.pop()
                result.append(node.value)
                node = node.right
            else:
                break

        return result

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
# print bst.findLeftSize(55)
min = bst.findmin()
for i in problem:
    print min,
    min = bst.successor(min)
print ''

max = bst.findmax()
for i in problem:
    print max,
    max = bst.predecessor(max)
print ''

print bst.sort()
print bst.inOrder_stack()
print bst.inOrder()

print bst.predecessor()
