def climbStairs(self, n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    r = [1, 2, 3]
    while 3 < n:
        r[0] = r[1] + r[2]
        r[1] = r[2] + r[0]
        r[2] = r[0] + r[1]
        n -= 3
    return r[n - 1]