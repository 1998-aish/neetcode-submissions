class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts={}
        for i,num in enumerate(nums):
            a=target-num
            if a in counts:
                return [counts[a],i]
            counts[num] = i
        
#time complexibitlity - o(n)
#space complexbility - o(n)

            
        