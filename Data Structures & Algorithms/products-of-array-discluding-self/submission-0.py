class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        res = [1] * len(nums)
        for idx in range(len(nums)):
            res[idx] *= pre
            pre *= nums[idx]
        print(res)
        for idx in range(len(nums)-1,-1,-1):
            res[idx] *= post
            post *= nums[idx]
        
        return res