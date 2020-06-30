class Solution:
    def lengthOfLongestSubstring(self, s) :
        number=0
        st=''
        max=0
        for i in s:
            if i not in st:
                st+=i
                number+=1
            else:
                if number>=max:
                    max=number
                index=st.index(i)
                st=st[(index+1):]+i
                number=len(st)

        if number>=max:
            max=number

        return max