class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target<i[-1]:
                for j in i:
                    if j==target:
                        return True
            elif target==i[-1]:
                return True
        return False
        