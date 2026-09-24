class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m: int = len(matrix) # rows
        n: int = len(matrix[0]) # columns
        full_len: int = m * n

        l: int = 0
        r: int = full_len - 1
        while l <= r:
            mid = (l + r) // 2
            row = mid // n
            column = mid - row * n
            if target < matrix[row][column]:
                r = mid - 1
            elif target > matrix[row][column]:
                l = mid + 1
            else:
                return True

        return False
