class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        list1,list2 = [],[]
        for i in s:
            list1.append(s.index(i))
        for i in pattern:
            list2.append(pattern.index(i))
        if(list1 == list2):
            list1,list2 = [],[]
            return True
        list1,list2 = [],[]

pattern = "abbd"
s = "dog cat cat dog"
obj = Solution()
print(obj.wordPattern(pattern,s))