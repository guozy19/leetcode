class Solution:
    def longestCommonPrefix(self, strs):
        if strs==[]:
            return ''
        n=len(min(strs))
        l=''
        for j in range(n):
            for word in strs:
                if len(l)<j+1:
                    l+=word[j]
                if l[j]!=word[j]:
                    l=l[:(len(l)-1)]
                    return l
        return l