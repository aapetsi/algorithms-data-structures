def quick_sort(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[0]
    lesser = [i  for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    print(lesser, greater)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)
    
print(quick_sort([10,4,4,5,9,22]))