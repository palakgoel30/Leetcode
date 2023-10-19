class Solution:
    def backspaceCompare(self,s,t):
        stack_s,stack_t = [],[]
        for i in s:
            if(i !='#'):
                stack_s.append(i)
            elif stack_s:
                stack_s.pop()

        for i in t:
            if(i !='#'):
                stack_t.append(i)
            elif stack_t:
                stack_t.pop()

        if(stack_s == stack_t):
            return True
        return False
s = 'a##c'
t = '#a#c'
obj = Solution()
print(obj.backspaceCompare(s,t))