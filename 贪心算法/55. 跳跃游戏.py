from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # 记录当前能到达的最远索引
        n = len(nums)
        
        for i in range(n):
            # 如果当前索引超过了能到达的最远位置，说明无法继续前进
            if i > max_reach:
                return False
            # 更新能到达的最远位置
            max_reach = max(max_reach, i + nums[i])
            # 如果已能到达或超过最后一个索引，直接返回True
            if max_reach >= n - 1:
                return True
        
        return max_reach >= n - 1