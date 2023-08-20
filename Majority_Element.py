def majorityElement(nums):
    counter = 0
    nums1 = set(nums)
    for i in nums1:
        x = nums.count(i)
        if(x>counter):
            counter = x
            num = i
    return num

nums = [2,2,1,1,3,2]
print(majorityElement(nums))

