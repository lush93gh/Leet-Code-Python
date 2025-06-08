from typing import Optional
from ListNode import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ans = ListNode(0)
        p3: ListNode = ans
        while l1 or l2 or carry > 0:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            sum = a + b + carry
            p3.next = ListNode(sum % 10)
            p3 = p3.next
            carry = sum // 10
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return ans.next