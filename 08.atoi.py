class Solution(object):
    def myAtoi(self, str):
        flag=1
        sum=0
        num=0
        if not str:
            return 0
        while str[0]==' ':
            str=str[1:]
            if not str:
                return 0
        if str[0]=='+':
            str=str[1:]
            flag=flag
            if not str or str[0] not in ['0','1','2','3','4','5','6','7','8','9']:
                return 0
        if str[0]=='-':
            str=str[1:]
            flag=-flag
        if not str:
            return 0
        while str[0]=='0':
            str=str[1:]
            if not str:
                return 0
        if str[0] not in ['1','2','3','4','5','6','7','8','9']:
            return 0
        for c in str:
            if c in ['0','1','2','3','4','5','6','7','8','9']:
                sum*=10
                num=int(c)
                sum+=num
            else:
                break
        sum=sum*flag
        if sum >(2**31-1):
            sum=2147483647
        if sum<(-(2**31)):
            sum=-2147483648
        return sum