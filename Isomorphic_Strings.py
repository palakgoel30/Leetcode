class Solution:
    def isIsomorphic(self,s,t):
        list1,list2 = [],[]
        for i in s:
            list1.append(s.index(i))
        for i in t:
            list2.append(t.index(i))
        if list1 == list2:

            return True
s = 'Paper'
t = 'Title'
obj = Solution()
print(obj.isIsomorphic(s,t))
