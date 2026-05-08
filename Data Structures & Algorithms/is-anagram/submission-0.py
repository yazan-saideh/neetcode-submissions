class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Sset = {}
        Tset = {}
        for i in s:
            Sset[i] = Sset.get(i,0) + 1
        for i in t:
            Tset[i] = Tset.get(i,0) + 1
        print(Sset)
        print(Tset)
        return Sset == Tset