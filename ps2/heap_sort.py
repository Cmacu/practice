class Heap:
    """
    A class representing an instance of a peak-finding problem.
    """

    def __init__(self, array):
        self.array = array
        self.build_max_heap()

    def build_max_heap(self):
        for i in range(len(self.array)/2, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, node):
        self.compare(node, node*2+1)
        self.compare(node, node*2)

    def compare(self, nodeA, nodeB):
        if(nodeB < len(self.array) and self.array[nodeB] > self.array[nodeA]):
            self.swap(nodeA, nodeB)
            self.max_heapify(nodeB)
            return

    def swap(self, nodeA, nodeB):
        temp = self.array[nodeA]
        self.array[nodeA] = self.array[nodeB]
        self.array[nodeB] = temp
        return

    def heapsort(self):
        sorted = []
        while len(self.array) > 0:
            self.swap(len(self.array) - 1, 0)
            last = self.array.pop()
            sorted.append(last)
            self.max_heapify(0)

        return sorted

    def printHeap(self):
        print self.array


def main():
    problem = [1, 12, 3, 10, 15, 6, 7, 8, 9]
    heap = Heap(problem)
    heap.printHeap()
    sorted = heap.heapsort()
    print sorted


if __name__ == "__main__":
    main()
