def binary_search(arr, target, start, end):

    if start > end:
        return -1
    midpoint = (start + end) // 2

    if target == arr[midpoint]:
        return midpoint
    elif target < arr[midpoint]:
        return binary_search(arr, target, start, midpoint - 1)
    
    else:
        return binary_search(arr, target, midpoint + 1, end)
    



lst = [1,2,3,4,5,6,12,13,22,33]

result = binary_search(lst, 2, 0, len(lst) - 1)
print(result)