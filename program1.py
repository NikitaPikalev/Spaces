def binary_search(arr, k):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == k:
            return middle
        elif arr[middle] < k:
            left = middle + 1
        else:
            right = middle - 1

    return -1

numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

target = 11
result = binary_search(numbers, target)

if result != -1:
    print(f"Элемент {target} найден на позиции {result}")
else:
    print(f"Элемент {target} не найден")
