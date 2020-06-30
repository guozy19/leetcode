class Solution(object):
    def reverse(self, x):
        flag = 1
        p = 0
        l = []
        s = 0
        k = 1
        if x < 0:
            flag = -flag
            x = -x
        if x >= 2147483648 or x == 0:
            return 0
        for i in range(9, -1, -1):
            c = 10 ** i
            p = x // c
            l.append(x // c)
            x = x % c
        while l[0] == 0:
            del l[0]
        for j in l:
            s = s + j * k
            k = k * 10
        s = s * flag
        if s < -2147483648 or s > 2147483647:
            return 0
        return s
