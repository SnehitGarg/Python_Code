import random

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

n = 1000
array = [random.randint(1, 100) for i in range(n)]
sorted_array = insertion_sort(array)
print(*sorted_array)