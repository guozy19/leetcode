class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        big=[]
        small=[]
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                k=len(nums)-1
                p=j+1
                while k>=p:
                    if nums[i]+nums[j]+nums[k]==target or nums[i]+nums[j]+nums[p]==target:
                        return target
                    if k==p:
                        if nums[i]+nums[j]+nums[p]>target:
                            big.append(nums[i]+nums[j]+nums[p])
                        else:
                            small.append(nums[i]+nums[j]+nums[p])
                        break
                    if nums[i]+nums[j]+nums[k]<target:
                        small.append(nums[i]+nums[j]+nums[k])
                        break
                    if nums[i]+nums[j]+nums[p]>target:
                        big.append(nums[i]+nums[j]+nums[p])
                        break
                    if nums[i]+nums[j]+nums[k]>target and nums[i]+nums[j]+nums[p]<target:
                        big.append(nums[i]+nums[j]+nums[k])
                        small.append(nums[i]+nums[j]+nums[p])
                    k-=1
                    p+=1
        big.sort()
        small.sort()
        if big==[]:
            return small[len(small)-1]
        if small==[]:
            return big[0]
        if big[0]-target<=target-small[len(small)-1]:
            return big[0]
        else:
            return small[len(small)-1]
        return nums