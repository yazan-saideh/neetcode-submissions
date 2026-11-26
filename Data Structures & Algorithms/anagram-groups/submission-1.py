class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for i in s:
                key[ord("a") - ord(i)] += 1
            count[tuple(key)].append(s)
        return list(count.values())
            