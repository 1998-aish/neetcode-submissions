class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l=0
        r=len(height)-1
        leftmax=height[l]
        rigthmax=height[r]
        res=0
        while l<r:
            if leftmax < rigthmax:
                l+=1
                leftmax=max(leftmax,height[l])
                res+=leftmax-height[l]
            else:
                r-=1
                rigthmax=max(rigthmax,height[r])
                res+=rigthmax-height[r]

        return res