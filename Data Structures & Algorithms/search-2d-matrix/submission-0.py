class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u: int = 0
        d: int = len(matrix) - 1

        while u <= d:
            m_ud = (u + d) // 2
            row = matrix[m_ud]
            l: int = 0
            r: int = len(row) - 1
            while l <= r:
                m = (l + r) // 2
                if target < row[m]:
                    r = m - 1
                elif target > row[m]:
                    l = m + 1
                else:
                    return True
            if r < 0:
                d = m_ud - 1
            elif l > len(row) - 1:
                u = m_ud + 1
            else:
                break
        
        return False