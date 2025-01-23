import random

def generate_matrix(rows, cols, min_value=0, max_value=10):
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

def cyclic_shift(matrix, shift):
    rows = len(matrix)
    shift = shift % rows
    return matrix[-shift:] + matrix[:-shift]

rows = 6
cols = 6

# Генерация матрицы
matrix = generate_matrix(rows, cols)
print("Сгенерированная матрица:")
for row in matrix:
    print(row)

shift = 1
shifted_matrix = cyclic_shift(matrix, shift)

print(f"\nМатрица после циклического сдвига на {shift} позицию(и):")
for row in shifted_matrix:
    print(row)