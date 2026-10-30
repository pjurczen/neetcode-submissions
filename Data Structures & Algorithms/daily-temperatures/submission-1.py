class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]

        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, i = stack.pop()
                result[i] = idx - i
            stack.append((temp, idx))
        
        return result