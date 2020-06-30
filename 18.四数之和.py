class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        ans=[]
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                for k in range(j+1,len(nums)-1):
                    l=k+1
                    r=len(nums)-1
                    while r>=l:
                        if nums[i]+nums[j]+nums[k]+nums[l]==target:
                            if [nums[i],nums[j],nums[k],nums[l]] not in ans:
                                ans.append([nums[i],nums[j],nums[k],nums[l]])
                            break
                        if nums[i]+nums[j]+nums[k]+nums[r]==target:
                            if [nums[i],nums[j],nums[k],nums[r]] not in ans:
                                ans.append([nums[i],nums[j],nums[k],nums[r]])
                            break
                        if nums[i]+nums[j]+nums[k]+nums[l]>target:
                            break
                        if nums[i]+nums[j]+nums[k]+nums[r]<target:
                            break
                        if nums[i]+nums[j]+nums[k]+nums[l]<target and nums[i]+nums[j]+nums[k]+nums[r]>target:
                            l+=1
                            r-=1
        return ans