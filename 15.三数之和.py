class Solution(object):
    def threeSum(self, nums):
        number=[]
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            F=i+1
            L=len(nums)-1
            while F<L:
                if (nums[i]+nums[F]+nums[L]==0):
                    if [nums[i],nums[F],nums[L]] not in number:
                        number.append([nums[i],nums[F],nums[L]])
                    while F<L and nums[L]==nums[L-1]:
                        L-=1
                    while F<L and nums[F]==nums[F+1]:
                        F+=1
                    L-=1
                    F+=1
                elif nums[i]+nums[F]+nums[L]>0:
                    L=L-1
                elif nums[i]+nums[F]+nums[L]<0:
                    F=F+1
        return number