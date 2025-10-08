from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) == 1:
            return 0 
        
        m = len(height)

        max_Area = 0

        current_Area = 0
        for i in range(m):
            for j in range(i+1, m):
                left = i
                right = j
                current_Area = (right - left) * min(height[left], height[right])
                if current_Area > max_Area:
                    max_Area = current_Area
                
        return max_Area