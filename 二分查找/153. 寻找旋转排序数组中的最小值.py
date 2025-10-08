from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -5000

        m = len(nums)

        # 当列表只有一个元素时，这个元素就是数组最小的元素
        if m == 1:
            return nums[0]

        # 当列表不只有一个元素时，需要进行判断
        # 循环依次比较第一个和第二个数的大小，如果第一个数小于第二个数的次数为m-1的话，则第一个数就是最小的
        # 如果第一个数小于第二个数的次数小于m-1的话，也就是中间出现过第一个数大于第二个数的情况，则这次比较的第二个数即为最小的
        count = 0
        nums_copy = nums.copy()

        while len(nums) > 1:
            if nums[0] < nums[1]:
                count += 1
                nums.pop(0)
            else:
                return nums[1]

        if count == m-1:
            return nums_copy[0]