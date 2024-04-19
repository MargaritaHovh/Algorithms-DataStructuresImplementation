def counting_sort(arr):
    max_val = max(arr)

    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_array = []
    for i in range(len(count)):
        sorted_array.extend([i] * count[i])   #list chenq kara append anenq, dra hamar extend enq ogtagorcum

    return sorted_array

input_array = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(input_array))



