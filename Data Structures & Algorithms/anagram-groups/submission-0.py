class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            s_count = [0] * 26
            for letter in s:
                s_count[ord(letter) - ord('a')] += 1
            groups[tuple(s_count)].append(s)
        return list(groups.values())
       