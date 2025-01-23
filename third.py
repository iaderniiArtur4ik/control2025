import random

def generate_matrix(rows, cols, min_value=0, max_value=10):
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

def sort_columns(matrix):
    transposed = list(zip(*matrix))
    sorted_transposed = [sorted(col) for col in transposed]
    return [list(row) for row in zip(*sorted_transposed)]

rows = 6
cols = 6

matrix = generate_matrix(rows, cols)
print("Сгенерированная матрица:")
for row in matrix:
    print(row)

sorted_matrix = sort_columns(matrix)

print("\nМатрица после сортировки по столбцам:")
for row in sorted_matrix:
    print(row)