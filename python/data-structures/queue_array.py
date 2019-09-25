class Queue:
    def __init__(self, size=24):
        self.list = [None] * size
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        if self.isFull():
            return False

        next = self.head + 1
        if next == len(self.list):
            next = 0

        if self.list[next] is not None:
            self.head = next

        self.list[self.head] = value

        return True

    def dequeue(self):
        if self.isEmpty():
            # self.head = 0
            # self.tail = 0
            return False

        value = self.list[self.tail]
        # SET EMPTY
        self.list[self.tail] = None

        next = self.tail + 1

        if next == len(self.list):
            next = 0

        if self.list[next] is not None:
            self.tail = next

        return value

    def isEmpty(self):
        if self.list[self.tail] is None:
            return True
        else:
            return False

    def isFull(self):
        next = self.head + 1
        if next == len(self.list):
            next = 0

        if self.list[next] is not None:
            return True

        return False

    def getUsed(self):
        # check how much is used
        used = self.head - self.tail
        if self.head > self.tail:
            used = self.head + self.tail

        return used + 1

    def __str__(self):
        return str(self.list)


q = Queue(4)
print '1', q.enqueue(1)
print '2', q.enqueue(2)
print '3', q.enqueue(3)
print '4', q.enqueue(4)
print '5', q.enqueue(5)

print q.dequeue()
print q

print '6', q.enqueue(6)
print q
for i in range(5):
    print q.dequeue()
    print q
    print 'head:', q.head, ' tail:', q.tail

    print q.dequeue()
    print q
    print 'head:', q.head, ' tail:', q.tail

    print q.dequeue()
    print q
    print 'head:', q.head, ' tail:', q.tail

    print i, q.enqueue(i)
    print q
