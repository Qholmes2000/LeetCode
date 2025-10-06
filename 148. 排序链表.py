class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return []
        
        listVal = []

        while head:
            listVal.append(head.val)
            head = head.next

        listVal.sort()

        dummy = ListNode(0)
        current = dummy
        for val in listVal:
            current.next = ListNode(val)
            current = current.next

        return dummy.next