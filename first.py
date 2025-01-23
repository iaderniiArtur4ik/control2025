from random import randint

def bubble_sort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

a = [randint(1, 99) for _ in range(10)]
print("Исходный массив:", a)

bubble_sort(a)
print("Массив после пузырьковой сортировки:", a)

a.sort()
print("Массив после встроенной сортировки:", a)