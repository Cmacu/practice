class DoubleStack:
    def __init__(self, size=24):
        self.list = [None] * size
        self.A = -1
        self.B = size

    def push(self, value, stack="A"):
        if self.isFull():
            return False

        if stack == 'A':
            self.A += 1
            self.list[self.A] = value
            return True

        if stack == 'B':
            self.B -= 1
            self.list[self.B] = value
            return True

        return False

    def pop(self,  stack="A"):
        if stack == 'A':
            if self.isEmptyA():
                return False

            value = self.list[self.A]
            self.list[self.A] = None
            self.A -= 1
            return value

        if stack == 'B':
            if self.isEmptyB():
                return False

            value = self.list[self.B]
            self.list[self.B] = None
            self.B += 1
            return value

        return False

    def isFull(self):
        if (self.B - self.A) <= 1:
            return True
        else:
            return False

    def isEmptyA(self):
        if self.A < 0:
            return True
        else:
            return False

    def isEmptyB(self):
        if self.B >= len(self.list):
            return True
        else:
            return False

    def isEmpty(self):
        if self.isEmptyA() and self.isEmptyB():
            return True
        else:
            return False

    def __str__(self):
        return str(self.list)


problem = [1, 2, 3, 4, 5, 6, 7, 11]

doubleStack = DoubleStack(6)
for i in problem:
    if i // 2:
        print i, doubleStack.push(i, 'B'), ' in B'
    else:
        print i, doubleStack.push(i, 'A'), ' in A'

print doubleStack, doubleStack.isEmpty(), doubleStack.isFull()

while not doubleStack.isEmptyA():
    print doubleStack.pop('A')

print doubleStack

doubleStack.push('test')

while not doubleStack.isEmptyB():
    print doubleStack.pop('B')

print doubleStack
