def isHappy(n) :
    str_n = '{}'.format(n)
    while (len(str_n) >= 1 and str_n not in ('1', '2', '3', '4', '5', '6', '8', '9')):
        sums = 0
        for i in str_n:
            sums += int(i) * int(i)
        print(sums)
        str_n = '{}'.format(sums)
    if (str_n == '1'):
        return True
n = 19
print(isHappy(n))