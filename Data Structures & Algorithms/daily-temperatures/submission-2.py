class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][0]:
                prev_val, prev_index = stack.pop()
                res[prev_index] = i - prev_index
            stack.append((v, i))
        return res

        
