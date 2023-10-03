class Solution:
    def reverseWords(self, s: str) -> str:
        rev = ""
        a = s.split(" ")
        for i in a:
            rev = rev + " "+ (i[::-1])
        return rev.strip()
s = "Let's take LeetCode contest"
obj = Solution()
print(obj.reverseWords(s))