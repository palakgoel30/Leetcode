def reverseWords(s):
    a = s.split(" ")
    s = []
    for i in a:
        if (i != ''):
            s.append(i)
    a = s[::-1]
    s = ''
    for i in a:
        s = s + " " + i
    return s.strip()

s = 'a good   example'
print(reverseWords(s))