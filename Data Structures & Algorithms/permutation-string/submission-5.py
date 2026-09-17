class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counter = {}
        window = {}

        for c in s1:
            s1_counter[c] = s1_counter.get(c, 0) + 1

        l = 0
        window_size = len(s1)

        for r in range(len(s2)):
            c = s2[r]
            window[c] = window.get(c, 0) + 1

            if r - l + 1 > window_size:
                left = s2[l]
                window[left] -= 1

                if window[left] == 0:
                    del window[left]

                l += 1

            if r - l + 1 == window_size and window == s1_counter:
                return True

        return False