def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


def find_maximum(numbers):
    if not numbers:
        raise ValueError("Список не должен быть пустым")

    bubble_sort(numbers)

    return numbers[-1]


numbers = [3, 5, 1, 8, 2, 7]
maximum = find_maximum(numbers)
print("Максимальное число в списке:", maximum)
print("Отсортированный список:", numbers)
print("")
print("пузырьковая сортировка легче")