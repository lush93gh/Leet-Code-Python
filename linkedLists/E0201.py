import ListNode

class E0201:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if head != None:
            hashset = set()
            pointer = head
            hashset.add(head.val)

            while pointer.next != None:
                next = pointer.next
                if next.val not in hashset:
                    hashset.add(next.val)
                    pointer = pointer.next
                else:
                    pointer.next = next.next

        return head