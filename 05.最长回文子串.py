class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        np = [n * [0] for _ in range(n)]
        l, r = 0, 0
        for i in range(1, n):
            for j in range(n - i):
                if s[j] == s[i + j] and (j + 1 >= i + j - 1 or np[j + 1][i + j - 1]):
                    np[j][i + j] = 1
                    l, r = j, i + j

        return s[l:r + 1]