class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result: list[list[int]] = []
        candidates.sort()

        candidates = [c for c in candidates if c <= target]

        numbers: list[int] = []
        def dfs(i: int, total: int) -> None:
            if total == target:
                result.append(numbers.copy())
                return
            if i == len(candidates) or total > target:
                return
            
            numbers.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            numbers.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)

        return result