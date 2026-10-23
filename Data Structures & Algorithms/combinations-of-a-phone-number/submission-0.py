class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping: dict[str, list[str]] = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        result: list[str] = []
        def _helper(i: int, combination: str) -> None:
            if len(combination) == len(digits) and combination:
                result.append(combination)
            
            for j in range(i, len(digits)):
                for k in mapping[digits[j]]:
                    combination += k
                    _helper(j+1, combination)
                    combination = combination[:-1]

        _helper(0, "")

        return result