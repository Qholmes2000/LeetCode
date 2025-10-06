class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return []
        
        listVal = []

        while head:
            listVal.append(head.val)
            head = head.next
        
        l = len(listVal)
        listVal.pop(l-n)

        dummy = ListNode(0)
        current = dummy
        for val in listVal:
            current.next = ListNode(val)
            current = current.next

        return dummy.next

        


###### 上面是本方法实现，并不是在原链表基础上进行的修改，而是将原链表的val复写为列表，之后再重新创建的新链表

"""
下面是使用一趟扫描实现的方法
"""

