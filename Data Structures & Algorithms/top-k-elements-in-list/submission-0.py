class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        counter = {}
        res = []
        for num in nums:
            counter[num] = counter.get(num,0) + 1
        for key, val in counter.items():
            freq[val].append(key)
        for idx in range(len(freq) - 1,0,-1):
            for num in freq[idx]:
                res.append(num)
                if len(res) == k:  
                    return res
                
        
        