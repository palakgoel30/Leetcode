def isPalindrome(s):
    s = s.lower()
    for i in s:
        """if(96>ord(i)<122 or 47> ord(i)<57):"""
        if (not i.isalnum()):
            s = s.replace(i, "")
    s1 = s[::-1]
    for i in range(0, len(s)):
        if (s[i] != s1[i]):
            return False
    return True

s = 'A man, a plan, a canal: Panama'
print(isPalindrome(s))