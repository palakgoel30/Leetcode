class Solution:
    def maxProductDifference(self, nums):
        nums.sort(reverse=True)
        print(nums)
        if(len(nums) >3):
            return (nums[0]*nums[1])-(nums[len(nums)-1] * nums[len(nums)-2])



nums = [5,6,2,7,4]
obj = Solution()
result_in = obj.maxProductDifference(nums)
print(result_in)