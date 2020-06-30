class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n=len(nums1)+len(nums2)
        k_1=(len(nums1)+len(nums2))//2
        k_2=(len(nums1)+len(nums2)+2)//2
        def findkth(nums1,nums2,k):
            if len(nums1)<len(nums2):
                nums1,nums2=nums2,nums1
            if len(nums2)==0:
                return nums1[k-1]
            if k==1:
                return min(nums1[0],nums2[0])
            p=min(k//2,len(nums2))
            if nums1[p-1]>=nums2[p-1]:
                return findkth(nums1,nums2[p:],k-p)
            else:
                return findkth(nums1[p:],nums2,k-p)
        if n%2==0:
            final=0.5*(findkth(nums1,nums2,k_1)+findkth(nums1,nums2,k_1+1))
        if n%2==1:
            final=findkth(nums1,nums2,k_2)
        return final