# Linear Search Algorithm
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


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


def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    if low == high:
        if arr[low] == target:
            return low
    else:
        mid = (low + high) // 2
        if target > arr[mid]:
            return binary_search_recursive(arr, target, mid + 1, high)
        elif target < arr[mid]:
            return binary_search_recursive(arr, target, low, mid - 1)
        elif target == arr[mid]:
            return mid


def nearest_mid(arr, low, high, target):
    return low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])


def interpolation_search(arr, target, low, high):
    if low > high:
        return -1
    if low == high:
        if arr[low] == target:
            return low
    else:
        mid = nearest_mid(arr, low, high, target)
        if target > arr[mid]:
            return binary_search_recursive(arr, target, mid + 1, high)
        elif target < arr[mid]:
            return binary_search_recursive(arr, target, low, mid - 1)
        elif target == arr[mid]:
            return mid


print(interpolation_search([1,2,3,4,5,6,7,8,9,10], 10, 0, 9))
