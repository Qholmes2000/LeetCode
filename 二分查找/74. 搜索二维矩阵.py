from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:  # 同时检查矩阵和第一行是否为空
            return False
        
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            # 检查目标是否可能在当前行
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                # 遍历当前行的所有元素
                for j in range(n):
                    if target == matrix[i][j]:
                        return True
                # 当前行遍历完仍未找到，继续下一行
        # 所有行都检查完仍未找到
        return False
                

