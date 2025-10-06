class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        listVal = []

        while head:
            val = head.val
            listVal.append(val)
            head = head.next
        
        l = len(listVal)

        if l // 2 != 0:
            return False
        else:
            for i in range(int(l/2)):
                if listVal[i] == listVal[l-i]:
                    return True
                else:
                    return False

