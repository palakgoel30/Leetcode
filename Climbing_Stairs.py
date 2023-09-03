def climbStairs(n):
    if n <= 2:
        return n
    p1 = 1
    p2 = 2
    current = 0
    for i in range(2, n):
        current = p1 + p2
        p1 = p2
        p2 = current
    return current


n = 2
print(climbStairs(n))
