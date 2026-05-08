class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = {nums[idx]:idx for idx in range(len(nums))}
        for idx in range(len(nums)):
            res = target - nums[idx]
            if res in nums_set and idx != nums_set[res]:
                return [idx,nums_set[res]]
        return -1 