# Bubble Sort Algorithm
def bubble_sort(arr):
    if len(arr) == 1:
        return arr
    for k in range(len(arr) - 1):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = temp

    return arr
