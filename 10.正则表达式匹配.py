class Solution:
    def isMatch(self, s, p):
        if not p: return not s

        first = (len(s) > 0) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first and self.isMatch(s[1:], p))

        return first and self.isMatch(s[1:], p[1:])