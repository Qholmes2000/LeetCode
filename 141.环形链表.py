class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        arrived = set()

        while head:
            if head in arrived:
                return True
            
            arrived.add(head)
            head = head.next

        return False