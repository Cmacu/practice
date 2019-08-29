class Stack:
    def __init__(self, size=24):
        self.list = [None] * size
        self.top = -1

    def push(self, value):
        if self.isFull():
            return False

        self.top += 1
        self.list[self.top] = value
        return True

    def pop(self):
        if self.isEmpty():
            return False

        value = self.list[self.top]
        self.list[self.top] = None
        self.top -= 1

        return value

    def isFull(self):
        if self.top >= len(self.list) - 1:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top < 0:
            return True
        else:
            return False

    def __str__(self):
        return str(self.list)


problem = [1, 2, 3, 4, 5, 6, 7, 11]

stack = Stack(6)
for i in problem:
    print i, stack.push(i)

print stack, stack.isEmpty(), stack.isFull()

while not stack.isEmpty():
    print stack.pop()
