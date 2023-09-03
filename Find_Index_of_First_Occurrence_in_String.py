def strStr(haystack, needle):
    x = len(needle)
    if (needle in haystack):
        for i in range(len(haystack)):
            if (haystack[i:(i + x)] == needle):
                # print(haystack[i:x])
                return i
    else:
        return -1

haystack = 'leetcode'
needle = "leeto"
print(strStr(haystack,needle))