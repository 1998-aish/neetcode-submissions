class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # arr=[]
        # sum1=1
        # prefix=1
        # for i,k in enumerate(nums):
        #     sum1=sum1*prefix
        #     for j in range(i+1, len(nums)):
        #         sum1=sum1*nums[j]
        #     arr.append(sum1)
        #     sum1=1
        #     prefix=prefix*nums[i]
        # return arr
        arr=[1]*(len(nums))
        prefix=1
        for i in range(len(nums)):
            arr[i]=prefix
            prefix=prefix*nums[i]
        postfix=1
        for i in range(len(nums) -1, -1 , -1):
            arr[i]=arr[i]*postfix
            postfix=postfix*nums[i]
        return arr




        