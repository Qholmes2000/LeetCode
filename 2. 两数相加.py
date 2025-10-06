class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_val_lst, l2_val_lst = [], []

        while l1:
            l1_val_lst.append(l1.val)
            l1 = l1.next
        
        while l2:
            l2_val_lst.append(l2.val)
            l2 = l2.next

        m, n = len(l1_val_lst), len(l2_val_lst)
        l1_value, l2_value = 0, 0 

        for i in range(m):
            l1_value += l1_val_lst[m-1-i] * 10 ** (m-1-i)

        for j in range(n):
            l2_value += l2_val_lst[n-1-j] * 10 ** (n-1-j)

        sum_l1_l2 = l1_value + l2_value

        def split_integer(n):
            # 将整数转换为字符串，然后遍历每个字符并转换回整数
            return [int(digit) for digit in str(abs(n))]
        
        result = split_integer(sum_l1_l2)
        result.reverse()

        head = ListNode(0)
        current = head
        for val in result:
            current.next = ListNode(val)
            current = current.next
        
        return head.next




        