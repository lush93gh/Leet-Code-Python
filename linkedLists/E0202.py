import ListNode

class E0202:
    def kthToLast(self, head: ListNode, k: int) -> int:
        pointer = head
        count = 0
        while pointer != None:
            count += 1
            pointer = pointer.next

        pointer = head
        for i in range(count - k):
            pointer = pointer.next
        
        return pointer.val