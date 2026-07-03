class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        dup = {}
        for r in range(len(s)):
            if s[r]  in dup:
                l = max(dup[s[r]] + 1,l)
            dup[s[r]] = r
            res = max(res,r-l + 1)
                
        return res