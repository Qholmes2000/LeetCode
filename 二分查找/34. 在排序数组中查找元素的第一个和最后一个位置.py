from typing import List

class Solution:
    # lower_bound 返回最小的满足 nums[i] >= target 的下标 i
    # 如果数组为空，或者所有数都 < target，则返回 len(nums)
    # 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums)  # 开区间 (left, right)
        while left + 1 < right:  # 区间不为空
            mid = (left + right) // 2
            # 循环不变量：
            # nums[left] < target
            # nums[right] >= target
            if nums[mid] >= target:
                right = mid  # 范围缩小到 (left, mid)
            else:
                left = mid  # 范围缩小到 (mid, right)
        # 循环结束后 left+1 = right
        # 此时 nums[left] < target 而 nums[right] >= target
        # 所以 right 就是第一个 >= target 的元素下标
        return right

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.lower_bound(nums, target)  # 选择其中一种写法即可
        if start == len(nums) or nums[start] != target:
            return [-1, -1]  # nums 中没有 target
        # 如果 start 存在，那么 end 必定存在
        end = self.lower_bound(nums, target + 1) - 1
        return [start, end]