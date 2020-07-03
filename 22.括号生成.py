class Solution:
    def generateParenthesis(self, n ):
        def gen(ans,left,right,brace):
            if left==0 and right==0:
                ans.append(brace)
                return
            if left>0:
                gen(ans,left-1,right,brace+'(')
            if left<right:
                gen(ans,left,right-1,brace+')')
        ans=[]
        gen(ans,n,n,'')
        return ans