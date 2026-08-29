class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for indx in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[indx]:
                temp, index = stack.pop()
                res[index] = indx - index
            stack.append([temperatures[indx],indx])
        return res
