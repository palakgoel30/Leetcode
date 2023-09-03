def longestCommonPrefix(strs):
    strs.sort()
    str3 = ""
    str1 = strs[0]
    str2 = strs[-1]
    for k in range(min(len(str1), len(str2))):
        if (str1[k] != str2[k]):
            return str3
        else:
            str3 = str3 + str1[k]
    return str3

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))