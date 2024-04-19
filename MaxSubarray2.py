def max_subarray_divide_conquer(nums, left, right):
    if left == right:
        return nums[left]
    
    mid = (left + right) // 2
    
    max_left_sum = max_subarray_divide_conquer(nums, left, mid)
    max_right_sum = max_subarray_divide_conquer(nums, mid + 1, right)
    
    max_cross_sum = cross_max_subarray(nums, left, mid, right)
    
    return max(max_left_sum, max_right_sum, max_cross_sum)

def cross_max_subarray(nums, left, mid, right):
    left_sum = float('-inf')
    sum = 0
    for i in range(mid, left - 1, -1):
        sum += nums[i]
        left_sum = max(left_sum, sum)
    
    right_sum = float('-inf')
    sum = 0
    for i in range(mid + 1, right + 1):
        sum += nums[i]
        right_sum = max(right_sum, sum)
    
    return left_sum + right_sum

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_divide_conquer(nums, 0, len(nums) - 1)
print("Maximum subarray sum:", result)




