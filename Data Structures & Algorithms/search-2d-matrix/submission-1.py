class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix), len(matrix[0])
        top, bot = 0 , len(matrix) - 1
        res = 0
        while top <= bot:
            m = top + ((bot - top)//2)
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                res = m
                break
            elif matrix[m][0] > target:
                bot = m - 1
            elif matrix[m][-1] < target:
                top = m + 1
        l , r = 0 , len(matrix[0]) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if matrix[res][m] < target:
                l = m + 1
            elif matrix[res][m] > target:
                r = m - 1
            else:
                return True
        return False

