def findTheDifference(s: str, t: str) -> str:
    dict1 = {}
    dict2 = {}
    for item in t:
        if (item in dict1):
            dict1[item] += 1
        else:
            dict1[item] = 1
    for item in s:
        if (item in dict2):
            dict2[item] += 1
        else:
            dict2[item] = 1

    for key, value in dict1.items():
        if key not in dict2 or value != dict2[key]:
            return key

s = 'abcd'
t='abcdef'
print(findTheDifference(s,t))





