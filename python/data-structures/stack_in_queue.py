class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class QueueStack:

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        return self.enqueue(value)

    def enqueue(self, value):
        node = Node(value)
        if self.head is None:
            self.tail = node
            self.head = node
        else:
            prev = self.head
            self.head.next = node
            self.head = node
            self.head.prev = prev

        return True

    def pop(self):
        if self.isEmpty():
            return False

        value = self.head.value
        prev = self.head.prev

        if prev is not None:
            prev.next = None
        else:
            self.tail = None

        self.head = prev

        return value

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


qs = QueueStack()
print '1', qs.enqueue(1)
print '2', qs.enqueue(2)
print '3', qs.enqueue(3)
print '4', qs.enqueue(4)
print '5', qs.enqueue(5)
print '5', qs.enqueue(5)
print '5', qs.push(5)
print '3', qs.push(3)
print '5', qs.push(5)
print '5', qs.enqueue(5)

print qs

print 'pop: ', qs.pop()
print 'pop: ', qs.pop()
print 'pop: ', qs.pop()
print 'pop: ', qs.pop()
print 'pop: ', qs.pop()
print qs
print 'dequeue: ',  qs.dequeue()
print qs

print '6', qs.enqueue(6)
print qs
for i in range(5):
    print 'dequeue: ',  qs.dequeue()
    print qs
    print 'tail:', qs.tail, ' head:', qs.head

    print 'dequeue: ',  qs.dequeue()
    print qs
    print 'tail:', qs.tail, ' head:', qs.head

    print 'dequeue: ',  qs.dequeue()
    print qs
    print 'tail:', qs.tail, ' head:', qs.head

    print i, qs.enqueue(i)
    print qs
