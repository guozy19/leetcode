class Solution(object):
    def twosum(self, nums, target):
        number = []
        sum=0
        length=len(nums)
        while length>1:
            for i in range(length-1):
                sum=nums[i]+nums[length-1]
                if sum==target:
                    number=[i,length-1]
                    break
                length-=1
        return number
