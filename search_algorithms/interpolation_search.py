# Interpolation Search Algorithm
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
