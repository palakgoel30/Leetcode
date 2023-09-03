def minSubArrayLen(target, nums):
    n = len(nums)
    left = sum = 0
    min_length = float('inf')
    for right in range(n):
        sum += nums[right]
        while sum >= target:
            min_length = min(min_length, right - left + 1)
            sum -= nums[left]
            left += 1

    return 0 if (min_length == float('inf')) else min_length


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(target, nums))
