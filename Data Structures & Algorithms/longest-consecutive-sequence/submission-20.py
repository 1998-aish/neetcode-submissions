class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # count=1
        # num=0
        # nums_set = set(nums)
        # if not nums:
        #     return 0
        # for i in nums_set:
        #     num=i+1
        #     if num in nums_set:
        #         count+=1
        # return count
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest