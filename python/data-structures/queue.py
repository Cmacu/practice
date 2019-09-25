class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        node = Node(value)
        if self.head is None:
            self.tail = node
            self.head = node
        else:
            self.head.next = node
            self.head = node

        return True

    def dequeue(self):
        if self.isEmpty():
            return False

        value = self.tail.value
        self.tail = self.tail.next

        if self.tail is None:
            self.head = None

        return value

    def isEmpty(self):
        if self.tail is None:
            return True
        else:
            return False

    def __str__(self):
        node = self.tail
        while node is not None:
            print node.value,
            node = node.next

        return ''


q = Queue()
print '1', q.enqueue(1)
print '2', q.enqueue(2)
print '3', q.enqueue(3)
print '4', q.enqueue(4)
print '5', q.enqueue(5)
print '5', q.enqueue(5)
print '5', q.enqueue(5)
print '5', q.enqueue(5)
print '5', q.enqueue(5)
print '5', q.enqueue(5)

print 'dequeue: ',  q.dequeue()
print q

print '6', q.enqueue(6)
print q
for i in range(5):
    print 'dequeue: ',  q.dequeue()
    print q
    print 'tail:', q.tail, ' head:', q.head

    print 'dequeue: ',  q.dequeue()
    print q
    print 'tail:', q.tail, ' head:', q.head

    print 'dequeue: ',  q.dequeue()
    print q
    print 'tail:', q.tail, ' head:', q.head

    print i, q.enqueue(i)
    print q
