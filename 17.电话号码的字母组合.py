class Solution:
    def letterCombinations(self, digits) :
        tele={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if digits=='':
            return []
        ans=['']
        for i in digits:
            ans=[k+j for k in ans for j in tele[i]]
        return ans