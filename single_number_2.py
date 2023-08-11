class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dict = {}
        for item in nums:
            if(item in dict):
                dict[item] +=1
                #print('itemif',item)
            else:
                dict[item] = 1
                #print('itemelse',item)
        for key,value in dict.items():
            #print("%d" %(key))
            if(value == 1):
                return key
p = Solution()
print(p.singleNumber(nums=[2,2,3,2]))
