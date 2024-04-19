def merge_sort(arr, start, end):
    if start < end:           
        mid = (start + end) // 2
        merge_sort(arr, start, mid)   
        merge_sort(arr, mid + 1, end)  
        merge(arr, start, mid, end)

    else:
        return 
    
def merge(arr, start, mid, end):
        first1 = start
        last1 = mid
        first2 = mid + 1
        last2 = end
        temp = []
        
        while first1 <= last1 and first2 <= last2:
            if arr[first1] <= arr[first2]:
                temp.append(arr[first1])
                first1 += 1
            else:
                temp.append(arr[first2])
                first2 += 1

        while first1 <= last1:
            temp.append(arr[first1])
            first1 += 1

        while first2 <= last2:
            temp.append(arr[first2])
            first2 += 1

        for i in range(len(temp)):
            arr[start + i] = temp[i]

arr = [1, 4, 9, 2, 5, 11]
merge_sort(arr, 0, len(arr) - 1)
print(arr)
