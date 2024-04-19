# def max_subarray_bruteforce(nums):
#     max_sum = float("-inf")

#     for i in range(len(nums)):
#         current_sum = 0

#         for j in range(i, len(nums)):
#             current_sum += nums[j]
#             max_sum = max(max_sum, current_sum)

#     return max_sum

# nums = [7,1,-33,3,6,4]
# result = max_subarray_bruteforce(nums)
# print("Maximum subarray sum:", result)



def max_subarray_bruteforce(nums):
    max_sum = float("-inf")

    for i in range(len(nums)):
        current_sum = 0

        for j in range(i, len(nums)):
            current_sum +=nums[j]
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum


nums = [7,1,-33,3,6,4]
print(max_subarray_bruteforce(nums))
