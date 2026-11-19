class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #[3, 6, 7, 11]
        #[1,2,3,4,5,6,7,8,9,10,11]
        l=1
        r=max(piles)
        res=r
        while l<=r:# uses log m becz of binryy search
            m=(l+r)//2
            hours=0
            for i in piles:# use o(n)
                hours+= math.ceil(i/m)
            if hours<=h:
                res=min(res,m)
                r=m-1
            else:
                l=m+1
        return res
            
#time = o(n*log m) = o(nlogm)
#space=o(1)


