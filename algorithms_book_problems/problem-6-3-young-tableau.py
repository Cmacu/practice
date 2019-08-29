problem = [9, 16, 3,  2, 4, 8, 5, 2, 14, 23, 11]


class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def getValue(self, table):
        return table[self.row][self.col]

    def setValue(self, table, value):
        table[self.row][self.col] = value

    def isEqual(self, cell):
        if self.row == cell.row and self.col == cell.col:
            return True
        else:
            return False

    def __str__(self):
        return str(self.row) + ', ' + str(self.col)


class YoungTableau:
    def __init__(self, cols=4, rows=4):
        self.cols = cols
        self.rows = rows
        self.empty = float('inf')

        self.table = []
        for row in range(rows):
            a = []
            for col in range(cols):
                a.append(self.empty)
            self.table.append(a)

        self.lastCol = -1
        self.lastRow = 0

        return

    def setValue(self, cell, value):
        cell.setValue(self.table, value)

    def getValue(self, cell):
        return cell.getValue(self.table)

    def min_heapify(self, cell):
        if cell.row >= self.rows or cell.col >= self.cols:
            return

        cellMin = Cell(cell.row, cell.col)
        # RIGHT
        if cell.col + 1 < self.cols:
            cellMin = self.min_compare(Cell(cell.row, cell.col + 1), cellMin)
        # DOWN
        if cell.row + 1 < self.rows:
            cellMin = self.min_compare(Cell(cell.row + 1, cell.col), cellMin)

        if cell.isEqual(cellMin) is False:
            self.swap(cellMin, cell)
            self.min_heapify(cellMin)

    def max_heapify(self, cell):
        if cell.row <= 0 and cell.col <= 0:
            return

        cellMin = Cell(cell.row, cell.col)

        # UP
        if cell.row - 1 >= 0:
            cellMin = self.max_compare(Cell(cell.row - 1, cell.col), cellMin)
        # LEFT
        if cell.col - 1 >= 0:
            cellMin = self.max_compare(Cell(cell.row, cell.col - 1), cellMin)

        if cell.isEqual(cellMin) is False:
            self.swap(cellMin, cell)
            self.max_heapify(cellMin)

    def insert(self, value):
        if self.lastCol + 1 < self.cols:
            # RIGHT
            self.lastCol += 1
        elif self.lastRow + 1 < self.rows:
            # DOWN
            self.lastCol = 0
            self.lastRow += 1
        else:
            return False

        cell = Cell(self.lastRow, self.lastCol)
        self.setValue(cell, value)
        self.max_heapify(cell)

    def sort(self):
        sorted = []
        while True:
            value = self.extract()
            if value is None:
                break
            sorted.append(value)

        return sorted

    def find(self, value, cell=Cell(0, 0)):
        if cell.row >= self.rows or cell.col >= self.cols:
            return

        cellValue = self.getValue(cell)
        print cell, ': ', cellValue
        if cellValue == value:
            return cell

        if cellValue > value:
            return
        # FIND DOWN
        found = self.find(value, Cell(cell.row + 1, cell.col))
        if found is not None:
            return found
        # FIND RIGHT
        found = self.find(value, Cell(cell.row, cell.col + 1))
        if found is not None:
            return found

    def extract(self):
        firstCell = Cell(0, 0)
        min = self.getValue(firstCell)

        if min == self.empty:
            return None

        self.setValue(firstCell, self.empty)
        self.min_heapify(firstCell)

        return min

    def swap(self, cellA, cellB):
        temp = self.getValue(cellA)
        self.setValue(cellA, self.getValue(cellB))
        self.setValue(cellB, temp)

    def min_compare(self, cellA, cellB):
        if self.getValue(cellA) > self.getValue(cellB):
            return cellB
        else:
            return cellA

    def max_compare(self, cellA, cellB):
        if self.getValue(cellA) < self.getValue(cellB):
            return cellB
        else:
            return cellA

    def __str__(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print str(self.getValue(Cell(row, col))).ljust(3),

            print ''

        return ''


print problem
young_tableau = YoungTableau()
print young_tableau
for i in problem:
    print i
    if young_tableau.insert(i) is False:
        print 'Not inserted'
        break
    print young_tableau

print young_tableau.find(5)
print young_tableau.sort()
