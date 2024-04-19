def binary_search(lst, target):
    start = 0
    end = len(lst) - 1

    while start <= end:
        midpoint = (start+end) // 2

        if target == lst[midpoint]:
            return midpoint
    
        elif target < lst[midpoint]:
            end = midpoint - 1

        else:
            start = midpoint + 1

    return -1


lst = [1,2,3,4,5,6,12,13,22,33]

result = binary_search(lst, 1)

print(result)
