class Solution:
    def isValid(self, s):
        stack=[]
        d={')':'(',']':'[','}':'{'}
        if str=='':
            return True
        for c in s:
            if c in [')',']','}']:
                if stack==[] or stack[-1]!=d[c]:
                    return False
                if stack[-1]==d[c]:
                    del stack[-1]
            else:
                stack.append(c)
        if stack==[]:
            return True
        else:
            return False