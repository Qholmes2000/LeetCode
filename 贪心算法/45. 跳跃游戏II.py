from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_reach = 0  # 记录当前能到达的最远索引
        n = len(nums)
        jump_step = 0  # 记录总条约步数
        end = 0

        for i in range(n-1):
            max_reach = max(max_reach, i + nums[i])

            if i == end:
                end = max_reach
                jump_step += 1
                
                if end >= n - 1:
                    break
        return jump_step
