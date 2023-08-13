def removeElement(nums,val):
    while val in nums:
        nums.remove(val)
    return nums

nums = [3,6,6,4,6]
val = 6
print(removeElement(nums,val))