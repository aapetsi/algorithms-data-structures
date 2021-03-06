def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(a, b):
    ret = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ret.append(a[i])
            i += 1
        elif a[i] > b[j]:
            ret.append(b[j])
            j += 1

    while i < len(a):
        ret.append(a[i])
        i += 1

    while j < len(b):
        ret.append(b[j])
        j += 1
    print(ret)
    return ret
