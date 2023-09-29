class Solution:
    def isMonotonic(self, nums) -> bool:
        if len(nums) <2:
            return True
        pointer = 0
        for i in range(len(nums)-1):
            if(nums[i] < nums[i+1]):
                if pointer == 0:
                    pointer = 1
                elif pointer == -1:
                    return False
            if(nums[i] > nums[i+1]):
                if pointer == 0:
                    pointer = -1
                elif pointer == 1:
                    return False

        return True

nums = [1,2,2,9]
obj = Solution()
print(obj.isMonotonic(nums))