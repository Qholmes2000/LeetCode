from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        answer = [0] * length  # 初始化结果数组，默认0
        stack = []  # 存储索引，维持温度单调递减
        
        for i in range(length):
            # 当前温度大于栈顶索引对应的温度时，计算天数差
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)  # 当前索引入栈
        
        return answer