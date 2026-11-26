class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = {}
        t_counter = {}
        for i in s:
            s_counter[i] = s_counter.get(i,0) + 1
        for i in t:
            t_counter[i] = t_counter.get(i,0) + 1
        return s_counter == t_counter
    