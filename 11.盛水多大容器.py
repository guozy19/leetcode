class Solution(object):
    def maxArea(self, height):
        n=len(height)
        s=0
        for i in range(n):
            if height[0]>=height[len(height)-1]:
                t=height[len(height)-1]*(len(height)-1)
                del height[len(height)-1]
            else:
                t=height[0]*(len(height)-1)
                del height[0]
            if t>s:
                s=t
        return s