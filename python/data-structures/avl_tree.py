DEFAULT_K = 3


class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.k = DEFAULT_K
        self.size = 0
        self.level = 1
        self.position = 0
        return

    def insert(self, current, new):
        inserted = 0
        if new.value >= current.value + current.k:
            if current.right is None:
                new.parent = current
                new.position = 1
                current.right = new
                inserted = 1
            else:
                current.right, inserted = self.insert(current.right, new)
        elif new.value <= current.value - current.k:
            if current.left is None:
                new.parent = current
                new.position = -1
                current.left = new
                inserted = 1
            else:
                current.left, inserted = self.insert(current.left, new)

        current.level = self.getLevel(current)
        current.size += inserted

        # balance AVL tree
        current = self.balanceAVL(current)

        return current, inserted

    def getBalance(self, node):
        if node is None:
            return 0

        rightLevel = 0 if node.right is None else node.right.level
        leftLevel = 0 if node.left is None else node.left.level
        balance = rightLevel - leftLevel

        return balance

    def getLevel(self, node):
        if node is None:
            return 0

        leftLevel = 0 if node.left is None else node.left.level
        rightLevel = 0 if node.right is None else node.right.level
        max = leftLevel if leftLevel > rightLevel else rightLevel

        return 1 + max

    def balanceAVL(self, node):
        if node is None:
            return

        balance = self.getBalance(node)
        # print 'balance (' + str(node.value) + '): ' + str(balance)

        if balance > 1:
            # print 'right heavy: ' + str(node.value)
            # print self.traverse()
            if self.getBalance(node.right) >= 0:
                # print 'left rotate'
                node = self.leftRotate(node)
            else:
                # print 'right rotate'
                self.rightRotate(node.right)
                # print self.traverse()
                # print 'left rotate'
                node = self.leftRotate(node)

        if balance < -1:
            # print 'left heavy: ' + str(node.value)
            if self.getBalance(node.left) <= 0:
                # print 'right rotate'
                node = self.rightRotate(node)
            else:
                # print 'left rotate'
                self.leftRotate(node.left)
                # print 'right rotate'
                node = self.rightRotate(node)

        return node

    def rightRotate(self, node):
        x = node
        y = node.left
        P = node.parent
        B = None if node.left is None else node.left.right

        # update parent
        if P is not None:
            if x.position > 0:
                P.right = y
            else:
                P.left = y
        y.position = x.position
        y.parent = P

        # move B to x left child
        x.left = B
        if B is not None:
            B.parent = x
            B.position = -1

        # swap x and y
        y.right = x
        x.parent = y
        x.position = 1

        # update sizes
        x.level = self.getLevel(x)
        y.level = self.getLevel(y)

        return y

    def leftRotate(self, node):
        x = node
        y = node.right
        P = node.parent
        B = None if node.right is None else node.right.left

        # update parent
        if P is not None:
            if x.position > 0:
                P.right = y
            else:
                P.left = y
        y.parent = P
        y.position = x.position

        # move B to x right chlid
        x.right = B
        if B is not None:
            B.parent = x
            B.position = 1

        # swap x and y
        y.left = x
        x.parent = y
        x.position = -1

        # update sizes
        x.level = self.getLevel(x)
        y.level = self.getLevel(y)

        return y

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

    def traverse(self, node=None, indent=1):
        if node is None:
            node = self

        balance = self.getBalance(node)

        parentInfo = ''
        if node.parent is not None:
            parentInfo = '^' + str(node.parent.value)
        print '  ' * indent + \
            str(node.value) + '(' + str(balance) + \
            ',' + str(node.level) + ')' + parentInfo
        indent += 1
        if node.left is not None:
            node.traverse(node.left, indent)
        if node.right is not None:
            node.traverse(node.right, indent)


problem = [20, 65, 11, 29, 50, 35, 32, 55, 8, 5, 2, 25, 14, 17, 16]
bst = Node(41)

for i in problem:
    node = Node(i)
    # print i
    bst, inserted = bst.insert(bst, node)
    # print 'Inserted' if inserted else 'Not Inserted'

bst.traverse()
print 'Min:' + str(bst.findmin())
print 'Max:' + str(bst.findmax())
print 'Size left: ' + str(bst.findLeftSize(55))
print 'Sorted:'
print bst.sort()
