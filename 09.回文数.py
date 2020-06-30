class Solution(object):
    def isPalindrome(self, x):
        l=[]
        if x<0:
            return False
        if x==0:
            return True
        while x >0:
            l.append(x%10)
            x=x//10
        if len(l)==1:
            return True
        while l!=[]:
            if l[0]==l[-1]:
                del l[0]
                del l[-1]
                if len(l)==1:
                    break
            else:
                return False
        return True