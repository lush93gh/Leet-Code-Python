# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class M142:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while slow or fast:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                return None
            if fast:
                slow = slow.next
            else:
                return None

            if slow == fast:
                slow = head
                break
        
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow