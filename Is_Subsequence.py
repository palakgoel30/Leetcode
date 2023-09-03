def isSubsequence(s, t):
    for i in s:
        res = t.find(i)
        if res == -1:
            return False
        else:
            t = t[res + 1:]
    return True


s = 'abc'
t = 'ahbgdc'
print(isSubsequence(s, t))
