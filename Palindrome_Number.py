def isPalindrome(x):
    x1 = x
    num = 0
    if (x < 0):
        return False
    else:
        while (x != 0):
            digit = x % 10
            num = num * 10 + digit
            x = x // 10
    if (x1 == num):
        return True

x = 121
print(isPalindrome(x))