def maxSubArray(nums):
    flag = True
    maximum = -22222
    sum = 0
    for i in nums:
        if (i > 0):
            flag = False
            break
    if (flag == True):
        maximum = max(nums)
    else:
        for j in range(0, len(nums)):
            sum = sum + nums[j]
            if (sum < 0):
                sum = 0
            maximum = max(maximum, sum)

    return maximum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))