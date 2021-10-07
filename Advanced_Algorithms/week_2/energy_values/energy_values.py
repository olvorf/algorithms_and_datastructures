# python3

EPS = 1e-6
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row

def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def SelectPivotElement(pivot, a, used_rows):
    while pivot.row < len(a) and (used_rows[pivot.row] or a[pivot.row][pivot.column] == 0):
        pivot.row += 1
    #print(pivot.row)
    if pivot.row == len(a):
        return False
    else:
        return pivot

def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column

def ProcessPivotElement(a, b, pivot, used_rows):
    scale = a[pivot.row][pivot.column]
    if scale != 1:
        for i in range(len(a)):
            a[pivot.row][i] /= scale
        b[pivot.row] /= scale
    for i in range(len(a)):
        if i != pivot.row:
            multiple = a[i][pivot.column]
            for j in range(len(a)):
                a[i][j] -= a[pivot.row][j] * multiple
            b[i] -= b[pivot.row] * multiple
    used_rows[pivot.row] = True

#def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
#    used_rows[pivot_element.row] = True
#    used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)
    used_rows = [False] * size
    for i in range(size):
        pivot = Position(i, 0)
        pivot = SelectPivotElement(pivot, a, used_rows)
        if not pivot:
            return None
        else:
            #print(pivot.row, pivot.column)
            SwapLines(a, b, used_rows, pivot)
            ProcessPivotElement(a, b, pivot, used_rows)
            #print(a, b)
    return b

def PrintColumn(column):
    for e in column:
        print("{0:.6f}".format(e), end=' ')


if __name__ == '__main__':
    matrix = ReadEquation()
    solution = SolveEquation(matrix)
    PrintColumn(solution)
    exit(0)
