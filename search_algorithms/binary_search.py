# Binary Search Algorithm
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2
    while low <= high:
        if arr[mid] < target:
            low = mid + 1
            mid = (low + high) // 2
        elif arr[mid] > target:
            high = mid - 1
            mid = (low + high) // 2
        elif arr[mid] == target:
            return mid
    return -1
