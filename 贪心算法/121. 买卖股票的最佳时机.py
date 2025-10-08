from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0  # 不足两天无法交易
    
        min_price = prices[0]  # 初始化最低价格为第一天
        max_profit = 0         # 初始化最大利润为0
        
        for price in prices[1:]:
            if price < min_price:
                min_price = price  # 更新最低价格
            else:
                # 计算当前利润并更新最大利润
                current_profit = price - min_price
                if current_profit > max_profit:
                    max_profit = current_profit
        
        return max_profit
        


        