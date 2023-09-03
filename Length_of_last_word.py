def lengthOfLastWord(s) -> int:
    list1 = s.split(" ")
    val = ""
    while val in list1:
        list1.remove(val)
    return (len(list1[-1]))

s = '   fly me   to   the moon  '
print(lengthOfLastWord(s))