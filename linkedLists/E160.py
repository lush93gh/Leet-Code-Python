import ListNode

class E160:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        table = set()
        pointer = headA
        while pointer is not None:
            table.add(hash(pointer))
            pointer = pointer.next
        pointer = headB
        while pointer is not None:
            if hash(pointer) in table:
                return True
            pointer = pointer.next
        return False
