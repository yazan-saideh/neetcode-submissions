class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        for i,v in enumerate(nums):
            diff = target - v
            if diff in num:
                return [num[diff],i]
            num[v] = i
            