class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result: list[list[int]] = []
        subset: list[int] = []

        def _helper(i: int) -> None:
            if len(subset) == k:
                result.append(subset.copy())
                return
        
            for j in range(i, n+1):
                subset.append(j)
                _helper(j+1)
                subset.pop()

        _helper(1)

        return result