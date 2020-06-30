class Solution(object):
    def convert(self, s, numRows):
        res=[''for i in range(numRows)]
        if numRows<=1:
            return s
        num=0
        p=-1
        for j in s:
            res[num]+=j
            if num==0 or num==numRows-1:
                p=-p
            num+=p
        return ''.join(res)