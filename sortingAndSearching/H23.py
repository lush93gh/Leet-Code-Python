from typing import Optional
from typing import List
from ListNode import ListNode
from heapq import heapify, heappush, heappop

class H23:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = [(node.val, idx, node) for idx, node in enumerate(lists) if node != None]
        heapify(min_heap)
        pointer = head = ListNode(0)
        while min_heap:
            node_val, idx, node = heappop(min_heap)
            pointer.next = node
            pointer = pointer.next
            if node.next:
                next = node.next
                heappush(min_heap, (next.val, idx, next))
        return head.next

