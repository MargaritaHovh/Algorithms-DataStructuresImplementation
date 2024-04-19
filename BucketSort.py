import random

def insertion_sort(bucket):
    for j in range(1, len(bucket)):
        key = bucket[j]   
        i = j - 1 
        while i >= 0 and bucket[i] > key:       
            bucket[i+1] = bucket[i]
            i = i - 1
        bucket[i+1]= key       

def bucket_sort(arr, num_buckets=10):
    min_val = min(arr)
    max_val = max(arr)
    bucket_range = (max_val - min_val) / num_buckets    #haskananq te amen bucket qani tarr kara parunaki
 
    buckets = []
    for _ in range(num_buckets):
        buckets.append([])   #list e sarqum vori mej ka 10 hat datark list

    for num in arr:
        index = int((num - min_val) // bucket_range)
        index = min(index, num_buckets - 1) 
        buckets[index].append(num)

    for bucket in buckets:
        insertion_sort(bucket)

    sorted_arr = []
    for bucket in buckets:
        for num in bucket:
            sorted_arr.append(num)     #verjnakan listi mej hertov bolor bucketneri tarrery avelacnuma
    return sorted_arr


random_list = [random.randint(1, 1000) for _ in range(20)]
print("Original list:", random_list)

sorted_list = bucket_sort(random_list)
print("Sorted list:", sorted_list)

