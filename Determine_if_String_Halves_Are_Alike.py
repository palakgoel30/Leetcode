class Solution:
    def halvesAreAlike(self, s):
        n = int(len(s)/2)
        print(s[0:n])
        count,count1 = 0,0
        list1 = ['a','e','i','o','u','A','E','I','O','U']
        for i in s[0:n]:
            if(i in list1):
                count += 1
        for i in s[n:len(s)]:
            if(i in list1):
                count1 += 1
        if(count == count1):
            return True

s= 'Uo'
obj = Solution()
print(obj.halvesAreAlike(s))
