def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    ret = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        ret.append(arr.pop(smallest)) 
    return ret


print(selection_sort([5, 3, 6, 2, 10]))