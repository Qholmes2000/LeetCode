from typing import List
from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return [0]

        # 统计每个字母在整个字符串中的总出现次数
        total_count = defaultdict(int)
        for c in s:
            total_count[c] += 1
        
        current_count = defaultdict(int)  # 统计当前子串中每个字母的出现次数
        result = []
        start = 0  # 当前区间的起始索引
        
        for i, c in enumerate(s):
            current_count[c] += 1  # 更新当前子串中字母的计数
            
            # 检查当前子串中所有已出现的字母是否都达到了总次数
            # 如果所有字母都满足，则可以截断当前区间
            all_satisfied = True
            for char in current_count:
                if current_count[char] != total_count[char]:
                    all_satisfied = False
                    break
            
            if all_satisfied:
                result.append(i - start + 1)
                start = i + 1  # 开始下一个区间
                current_count.clear()  # 清空当前计数，准备统计新区间
        
        return result