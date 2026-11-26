class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = [0] * 26
        t_counter = [0] * 26
        for i in s:
            s_counter[ord("a") - ord(i)] += 1
        for i in t:
            t_counter[ord("a") - ord(i)] += 1
        return s_counter == t_counter
        
        
    