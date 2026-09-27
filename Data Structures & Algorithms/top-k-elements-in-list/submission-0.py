class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1:1, 2:2, 3:3 k=2
        #1:3 2:2 3:1 --> vale->key. arr[j]=i
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1

        arr= [[] for i in range(len(nums)+1)]
        for i,j in freq.items():
            arr[j].append(i)

        res=[]
        for i in range(len(arr)-1,0,-1):
            for num in arr[i]:
                res.append(num)   
            if len(res)==k:
                return res
            

