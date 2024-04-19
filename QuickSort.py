# first as a pivot

def partition(arr, first, last):   #en gorcoxutyuny vori yntacqum pivot index enq yntrum vor zc n kisenq
    pivot = arr[first]
    left = first + 1
    right = last
    
    while left <= right:
        while left <= right and arr[left] <= pivot:  #dzaxic pivotic mec tivna gtnum   #arajiny stugum enq vor lefty durs chga zc-ic
            left += 1
        while arr[right] >= pivot and right >= left:#ajic pivotic poqr tivy
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
    
    arr[first], arr[right] = arr[right], arr[first]  # qani vor pivotic poqr tivna, mi hatel pivoti het enq poxum
    return right

def quickSort(arr, first, last):
    if first < last:
        pivotIndex = partition(arr, first, last)  
        quickSort(arr, first, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, last)

arr = [4, 2, 9, 1, 6, 5, 3]
quickSort(arr, 0, len(arr) - 1)
print(arr)




#last as a pivot
# def partition(arr, first, last):
#     pivot = arr[last]
#     left = first
#     right = last - 1
    
#     while left <= right:
#         while left <= right and arr[left] <= pivot:  #dzaxic pivotic mec tivna gtnum   #arajiny stugum enq vor lefty durs chga zc-ic
#             left += 1
#         while arr[right] >= pivot and right >= left:#ajic pivotic poqr tivy
#             right -= 1
#         if left < right:
#             arr[left], arr[right] = arr[right], arr[left]
#     arr[left], arr[last] = arr[last], arr[left]  # qani vor pivotic mec tivna, mi hatel pivoti het enq poxum
#     return left

# def quickSort(arr, first, last):
#     if first < last:
#         pivotIndex = partition(arr, first, last)  #partitioni return arac arjeqna
#         quickSort(arr, first, pivotIndex - 1)
#         quickSort(arr, pivotIndex + 1, last)

# arr = [4, 2, 9, 1, 6, 5, 3]
# quickSort(arr, 0, len(arr) - 1)
# print(arr)




#Median of three
# def partition(arr, first, last):
#     pivot = arr[(first + last) // 2]
#     left = first
#     right = last
    
#     while left <= right:
#         while arr[left] < pivot:
#             left += 1
#         while arr[right] > pivot:
#             right -= 1
#         if left <= right:
#             arr[left], arr[right] = arr[right], arr[left]
#             left += 1
#             right -= 1
    
#     return left

# def quickSort(arr, first, last):
#     if first < last:
#         pivotIndex = partition(arr, first, last)
#         quickSort(arr, first, pivotIndex - 1)
#         quickSort(arr, pivotIndex, last) 

# arr = [5, 8, 27, 26, 4, 9, 6]
# quickSort(arr, 0, len(arr) - 1)
# print(arr)




#random
# import random
# def partition(arr, first, last):
#     pivot_index = random.randint(first, last)
#     pivot = arr[pivot_index]

#     arr[pivot_index], arr[last] = arr[last], arr[pivot_index]
#     left = first
#     right = last - 1
    
#     while left <= right:
#         while left <= right and arr[left] <= pivot:  #dzaxic pivotic mec tivna gtnum   #arajiny stugum enq vor lefty durs chga zc-ic
#             left += 1
#         while arr[right] >= pivot and right >= left:#ajic pivotic poqr tivy
#             right -= 1
#         if left < right:
#             arr[left], arr[right] = arr[right], arr[left]
#     arr[left], arr[last] = arr[last], arr[left]  # qani vor pivotic mec tivna, mi hatel pivoti het enq poxum
#     return left

# def quickSort(arr, first, last):
#     if first < last:
#         pivotIndex = partition(arr, first, last)  #partitioni return arac arjeqna
#         quickSort(arr, first, pivotIndex - 1)
#         quickSort(arr, pivotIndex + 1, last)

# arr = [4, 2, 9, 1, 6, 5, 3]
# quickSort(arr, 0, len(arr) - 1)
# print(arr)